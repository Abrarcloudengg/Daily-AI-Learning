"""The curriculum: the ordered subject list and each subject's topic list.

Reads are cached for the lifetime of the instance. The previous code re-read
and re-parsed the same JSON on every lookup, which meant rendering the README
opened and decoded all fifteen topic files twice.
"""

from __future__ import annotations

from dataclasses import dataclass
from functools import cached_property
from pathlib import Path

from .exceptions import CurriculumError
from .jsonio import read_json
from .logging_setup import get_logger
from .naming import lesson_folder_name, subject_slug
from .paths import Paths

__all__ = ["CatalogIssue", "TopicCatalog"]

logger = get_logger(__name__)


@dataclass(frozen=True)
class CatalogIssue:
    """A problem found by :meth:`TopicCatalog.validate`."""

    subject: str
    severity: str  # "error" or "warning"
    message: str

    def __str__(self) -> str:
        return f"[{self.severity}] {self.subject}: {self.message}"


class TopicCatalog:
    """Read-only view over ``config/subjects.json`` and the topic files."""

    def __init__(self, paths: Paths | None = None) -> None:
        self.paths = paths or Paths.discover()
        self._topics: dict[str, list[str]] = {}

    # ------------------------------------------------------------------
    # Subjects
    # ------------------------------------------------------------------
    @cached_property
    def subjects(self) -> list[str]:
        """The roadmap, in teaching order.

        Raises:
            CurriculumError: if the file is malformed, empty, or has duplicates.
        """
        raw = read_json(self.paths.subjects_file, description="subject list")

        if not isinstance(raw, dict) or "subjects" not in raw:
            raise CurriculumError(
                f'{self.paths.subjects_file} must be a JSON object with a "subjects" key.'
            )

        subjects = raw["subjects"]
        if not isinstance(subjects, list) or not subjects:
            raise CurriculumError(f'"subjects" in {self.paths.subjects_file} must be a non-empty list.')

        if any(not isinstance(item, str) or not item.strip() for item in subjects):
            raise CurriculumError(f'Every entry in "subjects" must be a non-empty string ({self.paths.subjects_file}).')

        duplicates = _duplicates(subjects)
        if duplicates:
            raise CurriculumError(
                f"Duplicate subject(s) in {self.paths.subjects_file}: {', '.join(duplicates)}. "
                "A repeated subject would be taught twice and break progress accounting."
            )

        # Two subjects sharing a slug would silently share one topic file.
        by_slug: dict[str, str] = {}
        for subject in subjects:
            slug = subject_slug(subject)
            if not slug:
                raise CurriculumError(f"Subject {subject!r} has no alphanumeric characters, so it has no topic file.")
            if slug in by_slug:
                raise CurriculumError(
                    f"Subjects {by_slug[slug]!r} and {subject!r} both resolve to the slug {slug!r} "
                    "and would share one topic file. Rename one of them."
                )
            by_slug[slug] = subject

        return list(subjects)

    def has_subject(self, subject: str) -> bool:
        return subject in self.subjects

    def index_of(self, subject: str) -> int:
        """Return the roadmap position of *subject*.

        Raises:
            CurriculumError: if the subject is not on the roadmap.
        """
        try:
            return self.subjects.index(subject)
        except ValueError as exc:
            raise CurriculumError(
                f"{subject!r} is not in {self.paths.subjects_file}. "
                f"Known subjects: {', '.join(self.subjects)}."
            ) from exc

    def next_subject(self, subject: str) -> str | None:
        """Return the subject following *subject*, or ``None`` at the end."""
        index = self.index_of(subject)
        if index + 1 >= len(self.subjects):
            return None
        return self.subjects[index + 1]

    # ------------------------------------------------------------------
    # Topics
    # ------------------------------------------------------------------
    def topics(self, subject: str) -> list[str]:
        """Return *subject*'s topics in teaching order.

        Raises:
            CurriculumError: if the topic file is missing or malformed.
        """
        cached = self._topics.get(subject)
        if cached is not None:
            return cached

        path = self.paths.topic_file(subject)
        if not path.exists():
            raise CurriculumError(
                f"No topic file for subject {subject!r}. Expected: {path}. "
                f"Create it with a JSON object of the form "
                f'{{"subject": "{subject}", "topics": ["..."]}}.'
            )

        topics = self._parse_topics(subject, path)
        self._topics[subject] = topics
        return topics

    def _parse_topics(self, subject: str, path: Path) -> list[str]:
        raw = read_json(path, description=f"topic file for {subject}")

        if not isinstance(raw, dict) or "topics" not in raw:
            raise CurriculumError(f'{path} must be a JSON object with a "topics" key.')

        topics = raw["topics"]
        if not isinstance(topics, list) or not topics:
            raise CurriculumError(f'"topics" in {path} must be a non-empty list.')

        if any(not isinstance(item, str) or not item.strip() for item in topics):
            raise CurriculumError(f"Every topic in {path} must be a non-empty string.")

        duplicates = _duplicates(topics)
        if duplicates:
            raise CurriculumError(
                f"Duplicate topic(s) in {path}: {', '.join(duplicates)}. "
                "Duplicates would generate the same lesson twice."
            )

        declared = raw.get("subject")
        if isinstance(declared, str) and declared != subject:
            # A copy-paste slip here silently teaches the wrong curriculum:
            # dsa_topics.json once declared "Node.js" and held Node.js topics.
            logger.warning(
                'Topic file %s declares subject "%s" but is loaded for "%s". '
                "Check that its contents match the subject.",
                path,
                declared,
                subject,
            )

        return list(topics)

    def topic_count(self, subject: str) -> int:
        """Return the number of topics for *subject*, or ``0`` if unreadable."""
        try:
            return len(self.topics(subject))
        except CurriculumError:
            return 0

    def total_topics(self) -> int:
        """Total topics across the whole roadmap."""
        return sum(self.topic_count(subject) for subject in self.subjects)

    def lesson_folder(self, subject: str) -> str:
        """Directory name used for *subject* under ``generated/``."""
        return lesson_folder_name(subject)

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def validate(self) -> list[CatalogIssue]:
        """Check the whole curriculum and return every problem found.

        Unlike the accessors this never raises for per-subject problems: the
        point is to report all of them in one pass so ``daily-ai validate`` can
        show a complete list.
        """
        issues: list[CatalogIssue] = []

        try:
            subjects = self.subjects
        except CurriculumError as exc:
            return [CatalogIssue("<roadmap>", "error", str(exc))]

        seen_topic_sets: dict[tuple[str, ...], str] = {}

        for subject in subjects:
            try:
                topics = self.topics(subject)
            except CurriculumError as exc:
                issues.append(CatalogIssue(subject, "error", str(exc)))
                continue

            path = self.paths.topic_file(subject)
            raw = read_json(path, description=f"topic file for {subject}")
            declared = raw.get("subject") if isinstance(raw, dict) else None
            if declared != subject:
                issues.append(
                    CatalogIssue(
                        subject,
                        "error",
                        f'{path} declares subject "{declared}" but the roadmap entry is "{subject}".',
                    )
                )

            # Identical topic lists mean one file was copied over another.
            fingerprint = tuple(topics)
            twin = seen_topic_sets.get(fingerprint)
            if twin is not None:
                issues.append(
                    CatalogIssue(
                        subject,
                        "error",
                        f"Topic list is identical to {twin!r}. One file is a stale copy of the other.",
                    )
                )
            else:
                seen_topic_sets[fingerprint] = subject

            if len(topics) < 5:
                issues.append(
                    CatalogIssue(subject, "warning", f"Only {len(topics)} topic(s); the subject looks unfinished.")
                )

        return issues


def _duplicates(items: list[str]) -> list[str]:
    """Return values appearing more than once, preserving first-seen order."""
    seen: set[str] = set()
    repeated: list[str] = []
    for item in items:
        if item in seen and item not in repeated:
            repeated.append(item)
        seen.add(item)
    return repeated
