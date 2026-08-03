"""Deciding which lesson to generate next.

The rule is deliberately simple: walk the roadmap in order and return the first
topic that has no lesson file. Because the check is against the filesystem
rather than against bookkeeping, the selector is idempotent — running it twice
without generating anything returns the same answer, and a lost or truncated
``progress.json`` cannot cause a duplicate lesson.
"""

from __future__ import annotations

from dataclasses import dataclass

from .catalog import TopicCatalog
from .exceptions import CurriculumError
from .lessons import LessonLibrary
from .logging_setup import get_logger
from .paths import Paths
from .progress import Progress, ProgressStore

__all__ = ["Selection", "TopicSelector"]

logger = get_logger(__name__)


@dataclass(frozen=True)
class Selection:
    """The next lesson to generate."""

    subject: str
    topic: str
    day: int
    #: Position of *topic* within its subject, one-based.
    topic_index: int
    #: Total topics in the subject, for progress display.
    topic_total: int

    def __str__(self) -> str:
        return f"{self.subject} day {self.day}: {self.topic} ({self.topic_index}/{self.topic_total})"


class TopicSelector:
    """Chooses the next topic and advances the roadmap when a subject ends."""

    def __init__(
        self,
        paths: Paths | None = None,
        catalog: TopicCatalog | None = None,
        library: LessonLibrary | None = None,
        store: ProgressStore | None = None,
    ) -> None:
        self.paths = paths or Paths.discover()
        self.catalog = catalog or TopicCatalog(self.paths)
        self.library = library or LessonLibrary(self.paths)
        self.store = store or ProgressStore(self.paths, self.catalog, self.library)

    def select(self, progress: Progress) -> Selection | None:
        """Return the next lesson, mutating *progress* as subjects complete.

        *progress* is advanced in place (``subject``, ``completed``,
        ``completed_subjects``) but never saved — persisting is the caller's
        decision, which keeps ``--dry-run`` genuinely side-effect free.

        Returns:
            The next :class:`Selection`, or ``None`` when the entire roadmap is
            finished.
        """
        self.store.reconcile(progress)

        # Bounded by the roadmap length: each iteration either returns or
        # advances to the next subject, so this cannot spin forever even if a
        # topic file goes missing halfway through.
        for _ in range(len(self.catalog.subjects) + 1):
            selection = self._first_unwritten(progress)
            if selection is not None:
                return selection

            if not self._advance_subject(progress):
                return None

        logger.error("Roadmap traversal did not terminate; treating the curriculum as complete.")
        return None

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------
    def _first_unwritten(self, progress: Progress) -> Selection | None:
        """Return the first topic of the current subject with no lesson file."""
        subject = progress.subject

        try:
            topics = self.catalog.topics(subject)
        except CurriculumError as exc:
            # Skip rather than abort: one broken topic file should not stop the
            # remaining subjects from ever being taught.
            logger.error("Skipping subject %s — %s", subject, exc)
            return None

        for index, topic in enumerate(topics, start=1):
            if self.library.exists(subject, topic):
                continue
            return Selection(
                subject=subject,
                topic=topic,
                day=progress.day,
                topic_index=index,
                topic_total=len(topics),
            )

        return None

    def _advance_subject(self, progress: Progress) -> bool:
        """Mark the current subject finished and move to the next one.

        Returns:
            ``True`` if *progress* now points at a new subject, ``False`` if the
            roadmap is exhausted.
        """
        finished = progress.subject

        if finished not in progress.completed_subjects:
            progress.completed_subjects.append(finished)

        try:
            following = self.catalog.next_subject(finished)
        except CurriculumError as exc:
            logger.error("Cannot advance past %s: %s", finished, exc)
            return False

        if following is None:
            logger.info("Every subject on the roadmap is complete.")
            return False

        logger.info("Finished %s — moving on to %s.", finished, following)

        progress.subject = following
        progress.current_topic = ""
        progress.completed = []

        # Rebuild `completed` for the new subject from whatever is already on
        # disk, so a partially generated subject resumes instead of restarting.
        self.store.reconcile(progress)
        return True
