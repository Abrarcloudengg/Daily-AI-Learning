"""Learning progress: the record of what has been taught.

``data/progress.json`` is generated state that is also committed, so it is a
permanent merge-conflict magnet: a scheduled GitHub Actions run and a local run
both rewrite it, and a botched conflict resolution silently truncates the
history. The defence is :meth:`ProgressStore.reconcile` — before any decision
is made, the recorded state is rebuilt from the lesson files that actually
exist. A corrupt or half-merged file therefore costs nothing: it is repaired on
the next run instead of causing duplicate lessons.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from .catalog import TopicCatalog
from .exceptions import ConfigurationError, CurriculumError, ProgressError
from .jsonio import read_json, write_json
from .lessons import LessonLibrary
from .logging_setup import get_logger
from .paths import Paths

__all__ = ["Progress", "ProgressStore", "ReconcileResult"]

logger = get_logger(__name__)


@dataclass
class Progress:
    """Where the learner is on the roadmap."""

    subject: str
    current_topic: str = ""
    completed: list[str] = field(default_factory=list)
    completed_subjects: list[str] = field(default_factory=list)

    @property
    def day(self) -> int:
        """The next lesson number within the current subject (one-based).

        Derived, never stored. Two independently-maintained counters — a stored
        ``day`` and ``len(completed) + 1`` — drifted apart until filenames and
        the README disagreed by seven days.
        """
        return len(self.completed) + 1

    @property
    def lessons_completed(self) -> int:
        """Lessons finished in the current subject."""
        return len(self.completed)

    # ------------------------------------------------------------------
    # Serialisation
    # ------------------------------------------------------------------
    @classmethod
    def from_dict(cls, raw: Any, *, default_subject: str) -> Progress:
        """Build a Progress from parsed JSON, tolerating missing keys.

        Unknown or wrongly-typed fields fall back to safe defaults rather than
        raising: an unattended daily job should heal itself, not halt.
        """
        if not isinstance(raw, dict):
            raise ProgressError(f"Progress file must contain a JSON object, got {type(raw).__name__}.")

        subject = raw.get("subject")
        if not isinstance(subject, str) or not subject.strip():
            logger.warning("Progress file has no usable `subject`; falling back to %r.", default_subject)
            subject = default_subject

        current_topic = raw.get("current_topic")
        if not isinstance(current_topic, str):
            current_topic = ""

        return cls(
            subject=subject,
            current_topic=current_topic,
            completed=_string_list(raw.get("completed"), "completed"),
            completed_subjects=_string_list(raw.get("completed_subjects"), "completed_subjects"),
        )

    def to_dict(self) -> dict[str, Any]:
        """Serialise for ``data/progress.json``.

        ``day`` is written even though it is derived: it is read by humans, by
        the README, and by the commit-message step in the workflow.
        """
        return {
            "subject": self.subject,
            "day": self.day,
            "current_topic": self.current_topic,
            "completed": list(self.completed),
            "completed_subjects": list(self.completed_subjects),
        }

    def copy(self) -> Progress:
        return Progress(
            subject=self.subject,
            current_topic=self.current_topic,
            completed=list(self.completed),
            completed_subjects=list(self.completed_subjects),
        )


@dataclass(frozen=True)
class ReconcileResult:
    """What :meth:`ProgressStore.reconcile` changed."""

    progress: Progress
    dropped: list[str]
    recovered: list[str]

    @property
    def changed(self) -> bool:
        return bool(self.dropped or self.recovered)


class ProgressStore:
    """Loads, repairs, and atomically saves :class:`Progress`."""

    def __init__(
        self,
        paths: Paths | None = None,
        catalog: TopicCatalog | None = None,
        library: LessonLibrary | None = None,
    ) -> None:
        self.paths = paths or Paths.discover()
        self.catalog = catalog or TopicCatalog(self.paths)
        self.library = library or LessonLibrary(self.paths)

    # ------------------------------------------------------------------
    # Load / save
    # ------------------------------------------------------------------
    def load(self) -> Progress:
        """Read progress from disk, creating a fresh record if absent."""
        default_subject = self.catalog.subjects[0]

        if not self.paths.progress_file.exists():
            logger.info("No progress file yet; starting the roadmap at %s.", default_subject)
            return Progress(subject=default_subject)

        try:
            raw = read_json(self.paths.progress_file, description="progress file")
        except ConfigurationError as exc:
            # A corrupt progress file must not end the run: everything it holds
            # can be rebuilt from `generated/` by reconcile().
            logger.warning("Progress file unreadable (%s); rebuilding it from generated lessons.", exc)
            return Progress(subject=default_subject)

        progress = Progress.from_dict(raw, default_subject=default_subject)

        if not self.catalog.has_subject(progress.subject):
            logger.warning(
                "Progress names subject %r which is not on the roadmap; resetting to %r.",
                progress.subject,
                default_subject,
            )
            progress.subject = default_subject
            progress.current_topic = ""

        progress.completed_subjects = [s for s in progress.completed_subjects if self.catalog.has_subject(s)]
        return progress

    def save(self, progress: Progress) -> None:
        """Persist *progress* atomically.

        Raises:
            ProgressError: if the file cannot be written.
        """
        try:
            write_json(self.paths.progress_file, progress.to_dict())
        except Exception as exc:
            raise ProgressError(f"Could not save progress to {self.paths.progress_file}: {exc}") from exc
        logger.debug("Saved progress: %s day %d.", progress.subject, progress.day)

    # ------------------------------------------------------------------
    # Reconciliation
    # ------------------------------------------------------------------
    def reconcile(self, progress: Progress) -> ReconcileResult:
        """Rebuild ``completed`` from the lessons present on disk.

        A topic counts as done only when its lesson file exists. This both
        drops phantom entries (recorded but no file, e.g. after a bad merge)
        and recovers real ones (file present but unrecorded, e.g. after a run
        that generated a lesson and then failed to commit).
        """
        try:
            topics = self.catalog.topics(progress.subject)
        except CurriculumError as exc:
            logger.warning("Cannot reconcile %s: %s", progress.subject, exc)
            return ReconcileResult(progress, dropped=[], recovered=[])

        actual = self.library.completed_topics(progress.subject, topics)
        previous = list(progress.completed)

        dropped = [topic for topic in previous if topic not in actual]
        recovered = [topic for topic in actual if topic not in previous]

        progress.completed = actual

        if progress.current_topic and progress.current_topic not in actual:
            progress.current_topic = actual[-1] if actual else ""

        if dropped:
            logger.warning(
                "%d topic(s) recorded as done have no lesson file and will be generated again: %s",
                len(dropped),
                ", ".join(dropped),
            )
        if recovered:
            logger.info(
                "%d lesson(s) found on disk but missing from progress; recorded them: %s",
                len(recovered),
                ", ".join(recovered),
            )

        return ReconcileResult(progress, dropped=dropped, recovered=recovered)

    def load_reconciled(self) -> ReconcileResult:
        """Convenience: :meth:`load` followed by :meth:`reconcile`."""
        return self.reconcile(self.load())

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------
    def global_completed(self, progress: Progress) -> int:
        """Lessons completed across the whole roadmap, not just this subject."""
        total = progress.lessons_completed
        for subject in progress.completed_subjects:
            if subject != progress.subject:
                total += self.catalog.topic_count(subject)
        return total


def _string_list(value: Any, field_name: str) -> list[str]:
    """Coerce *value* into a list of non-empty strings, warning on junk."""
    if value is None:
        return []
    if not isinstance(value, list):
        logger.warning("`%s` in the progress file is not a list; ignoring it.", field_name)
        return []

    cleaned: list[str] = []
    for item in value:
        if isinstance(item, str) and item.strip() and item not in cleaned:
            cleaned.append(item)
        else:
            logger.warning("Ignoring invalid entry in `%s`: %r", field_name, item)
    return cleaned
