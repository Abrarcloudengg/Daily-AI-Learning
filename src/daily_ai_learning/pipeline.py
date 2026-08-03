"""Orchestration: the only module that knows the order of operations.

A run is: reconcile → select → generate → quality-gate → write → record →
render README → commit. Each step is delegated; this file decides when they
happen, what a failure means, and what the caller is told afterwards.

The ordering is chosen so that a crash at any point is harmless. The lesson
file is written before progress is updated, so an interrupted run leaves a real
lesson that the next reconciliation picks up. Progress is never written for a
lesson that does not exist on disk.
"""

from __future__ import annotations

import time
from dataclasses import dataclass, field
from pathlib import Path

from .catalog import TopicCatalog
from .exceptions import LessonGenerationError
from .git_ops import GitRepository, is_ci
from .lessons import LessonLibrary
from .logging_setup import get_logger
from .paths import Paths
from .progress import Progress, ProgressStore
from .prompts import (
    LESSON_SECTIONS,
    SYSTEM_PROMPT,
    QualityReport,
    build_lesson_prompt,
    inspect_lesson,
)
from .provider import Completion, OpenRouterClient
from .readme import ReadmeRenderer
from .selector import Selection, TopicSelector
from .settings import Settings

__all__ = ["GeneratedLesson", "LessonPipeline", "RunReport"]

logger = get_logger(__name__)


@dataclass(frozen=True)
class GeneratedLesson:
    """One lesson successfully produced and written."""

    selection: Selection
    path: Path
    quality: QualityReport
    completion: Completion
    duration: float

    @property
    def commit_message(self) -> str:
        """Commit subject line, e.g. ``Day 9: While Loop (Python)``."""
        return f"Day {self.selection.day}: {self.selection.topic} ({self.selection.subject})"


@dataclass
class RunReport:
    """What a pipeline run accomplished."""

    lessons: list[GeneratedLesson] = field(default_factory=list)
    #: Why the run stopped: ``"completed"``, ``"roadmap-finished"``, ``"dry-run"``.
    reason: str = "completed"
    committed: bool = False
    pushed: bool = False

    @property
    def count(self) -> int:
        return len(self.lessons)


class LessonPipeline:
    """Generates lessons end to end."""

    def __init__(
        self,
        paths: Paths | None = None,
        settings: Settings | None = None,
        *,
        catalog: TopicCatalog | None = None,
        library: LessonLibrary | None = None,
        store: ProgressStore | None = None,
        selector: TopicSelector | None = None,
        client: OpenRouterClient | None = None,
        renderer: ReadmeRenderer | None = None,
        repository: GitRepository | None = None,
    ) -> None:
        """Collaborators are injectable so tests can substitute fakes."""
        self.paths = paths or Paths.discover()
        self.settings = settings or Settings.load(self.paths)
        self.catalog = catalog or TopicCatalog(self.paths)
        self.library = library or LessonLibrary(self.paths)
        self.store = store or ProgressStore(self.paths, self.catalog, self.library)
        self.selector = selector or TopicSelector(self.paths, self.catalog, self.library, self.store)
        self.renderer = renderer or ReadmeRenderer(
            self.paths, self.catalog, self.store, self.settings, self.library
        )
        self.repository = repository or GitRepository(self.paths, self.settings)
        self._client = client

    # ------------------------------------------------------------------
    # Lazily constructed so `--dry-run` and `readme` never need an API key
    # ------------------------------------------------------------------
    @property
    def client(self) -> OpenRouterClient:
        if self._client is None:
            self._client = OpenRouterClient(self.settings)
        return self._client

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def peek(self) -> Selection | None:
        """Return the next lesson without generating or saving anything."""
        return self.selector.select(self.store.load())

    def run(self, *, count: int = 1, dry_run: bool = False, use_git: bool = True) -> RunReport:
        """Generate up to *count* lessons.

        Args:
            count: Maximum lessons to produce this run.
            dry_run: Resolve the next topic and stop. No API call, no writes.
            use_git: Commit and push afterwards. Ignored under CI, where the
                workflow owns the commit step.

        Returns:
            A :class:`RunReport` describing what happened.

        Raises:
            ProviderError: the model provider failed after every retry.
            LessonGenerationError: a response arrived but was unusable.
        """
        report = RunReport()
        progress = self.store.load()

        for iteration in range(1, count + 1):
            selection = self.selector.select(progress)

            if selection is None:
                logger.info("🎓 The entire roadmap is complete — nothing left to generate.")
                report.reason = "roadmap-finished"
                break

            logger.info(
                "📚 %s · Day %d · %s  (%d/%d)",
                selection.subject,
                selection.day,
                selection.topic,
                selection.topic_index,
                selection.topic_total,
            )

            if dry_run:
                logger.info("Dry run: stopping before the API call. Nothing was written.")
                report.reason = "dry-run"
                break

            lesson = self._generate_one(selection, progress)
            report.lessons.append(lesson)

            if iteration < count:
                logger.info("— lesson %d of %d done —", iteration, count)

        if report.lessons:
            self.renderer.write(progress)
            self._finalise_git(report, use_git=use_git)

        return report

    # ------------------------------------------------------------------
    # Steps
    # ------------------------------------------------------------------
    def _generate_one(self, selection: Selection, progress: Progress) -> GeneratedLesson:
        """Produce, validate, write, and record a single lesson."""
        started = time.monotonic()

        prompt = build_lesson_prompt(selection.subject, selection.topic, selection.day)
        completion = self.client.complete(SYSTEM_PROMPT, prompt)

        quality = inspect_lesson(
            completion.content,
            selection.topic,
            finish_reason=completion.finish_reason,
            min_chars=self.settings.min_lesson_chars,
        )
        self._enforce_quality(selection, quality)

        path = self.library.write(
            selection.subject, selection.topic, selection.day, completion.content
        )
        logger.info("📝 Wrote %s", self.paths.relative(path))

        # Progress is recorded only after the file exists, so the two can never
        # disagree in the dangerous direction (recorded but not written).
        if selection.topic not in progress.completed:
            progress.completed.append(selection.topic)
        progress.current_topic = selection.topic
        self.store.save(progress)

        return GeneratedLesson(
            selection=selection,
            path=path,
            quality=quality,
            completion=completion,
            duration=time.monotonic() - started,
        )

    def _enforce_quality(self, selection: Selection, quality: QualityReport) -> None:
        """Reject unusable lessons; warn about imperfect ones.

        Raises:
            LessonGenerationError: when the lesson must not be written.
        """
        problems = quality.describe()

        if not quality.is_usable:
            raise LessonGenerationError(
                f"Lesson for {selection.subject} / {selection.topic} failed the quality gate: "
                + "; ".join(problems)
                + ".\n  Nothing was written. Raise `max_tokens` in config/settings.json and retry."
            )

        if self.settings.require_all_sections and quality.missing_sections:
            raise LessonGenerationError(
                f"Lesson for {selection.topic} is missing "
                f"{len(quality.missing_sections)} required section(s): "
                f"{', '.join(quality.missing_sections)}.\n"
                "  Set `require_all_sections` to false in config/settings.json to accept it anyway."
            )

        if problems:
            logger.warning("Accepted with warnings — %s.", "; ".join(problems))

        expected = len(LESSON_SECTIONS)
        logger.info(
            "✅ Quality gate passed: %d/%d sections, %d characters.",
            expected - len(quality.missing_sections),
            expected,
            quality.char_count,
        )

    def _finalise_git(self, report: RunReport, *, use_git: bool) -> None:
        """Commit and push, unless CI owns that step or the user opted out."""
        if not use_git:
            logger.info("Skipping git (--no-git). Changes are on disk but uncommitted.")
            return

        if is_ci():
            logger.info("Running in CI — the workflow will commit and push.")
            return

        if not self.repository.available:
            logger.info("Not a git repository; skipping commit.")
            return

        message = _commit_message(report.lessons)

        self.repository.sync()
        report.committed = self.repository.commit(message)

        if report.committed:
            report.pushed = self.repository.push()


def _commit_message(lessons: list[GeneratedLesson]) -> str:
    """Build a commit message for one or many lessons."""
    if len(lessons) == 1:
        return lessons[0].commit_message

    subjects = sorted({lesson.selection.subject for lesson in lessons})
    summary = f"Add {len(lessons)} lessons ({', '.join(subjects)})"
    body = "\n".join(
        f"- Day {lesson.selection.day}: {lesson.selection.topic} ({lesson.selection.subject})"
        for lesson in lessons
    )
    return f"{summary}\n\n{body}"
