"""The lesson library on disk.

``generated/`` is the project's real source of truth. ``data/progress.json`` is
a cache of it, and when the two disagree the files win — a lesson that exists
has been taught, whatever a JSON file says.

Directory listings are cached per subject. The old ``lesson_exists`` helper
called ``os.listdir`` once per topic, so picking the next Python topic issued
114 listings of the same directory on every run.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path

from .exceptions import LessonGenerationError
from .logging_setup import get_logger
from .naming import LESSON_FILENAME_PATTERN, lesson_filename, safe_topic_name
from .paths import Paths

__all__ = ["LessonFile", "LessonLibrary"]

logger = get_logger(__name__)


@dataclass(frozen=True)
class LessonFile:
    """A lesson that exists on disk."""

    path: Path
    day: int
    stem: str

    @property
    def size_bytes(self) -> int:
        return self.path.stat().st_size


class LessonLibrary:
    """Reads and writes lesson Markdown files."""

    def __init__(self, paths: Paths | None = None) -> None:
        self.paths = paths or Paths.discover()
        self._listing_cache: dict[str, dict[str, LessonFile]] = {}

    # ------------------------------------------------------------------
    # Reading
    # ------------------------------------------------------------------
    def lessons(self, subject: str) -> dict[str, LessonFile]:
        """Return ``{topic_stem: LessonFile}`` for *subject*.

        The result is cached; call :meth:`invalidate` after writing.
        """
        cached = self._listing_cache.get(subject)
        if cached is not None:
            return cached

        folder = self.paths.lesson_dir(subject)
        found: dict[str, LessonFile] = {}

        if folder.is_dir():
            for entry in sorted(folder.iterdir()):
                if not entry.is_file():
                    continue
                match = LESSON_FILENAME_PATTERN.match(entry.name)
                if match is None:
                    continue
                stem = match.group("stem")
                lesson = LessonFile(path=entry, day=int(match.group("day")), stem=stem)
                # Keep the lowest day number if a topic was written twice.
                existing = found.get(stem)
                if existing is None or lesson.day < existing.day:
                    found[stem] = lesson

        self._listing_cache[subject] = found
        return found

    def find(self, subject: str, topic: str) -> LessonFile | None:
        """Return the lesson file for *topic*, or ``None`` if not written yet."""
        return self.lessons(subject).get(safe_topic_name(topic))

    def exists(self, subject: str, topic: str) -> bool:
        """True when a lesson for *topic* has already been generated."""
        return self.find(subject, topic) is not None

    def completed_topics(self, subject: str, topics: list[str]) -> list[str]:
        """Filter *topics* down to those with a lesson on disk, order preserved."""
        written = self.lessons(subject)
        return [topic for topic in topics if safe_topic_name(topic) in written]

    def count(self, subject: str) -> int:
        """Number of lessons written for *subject*."""
        return len(self.lessons(subject))

    def total_count(self) -> int:
        """Number of lesson files across every subject folder."""
        if not self.paths.generated_dir.is_dir():
            return 0
        return sum(
            1
            for folder in self.paths.generated_dir.iterdir()
            if folder.is_dir()
            for entry in folder.iterdir()
            if entry.is_file() and LESSON_FILENAME_PATTERN.match(entry.name)
        )

    # ------------------------------------------------------------------
    # Writing
    # ------------------------------------------------------------------
    def write(self, subject: str, topic: str, day: int, content: str) -> Path:
        """Write a lesson and return its path.

        Args:
            subject: Owning subject; decides the destination folder.
            topic: Topic name; normalised into the file name.
            day: One-based lesson number within the subject.
            content: Markdown body.

        Raises:
            LessonGenerationError: if *content* is blank or the write fails.
        """
        if not content or not content.strip():
            raise LessonGenerationError(f"Refusing to write an empty lesson for {subject} / {topic}.")

        folder = self.paths.lesson_dir(subject)
        folder.mkdir(parents=True, exist_ok=True)
        destination = folder / lesson_filename(day, topic)

        # Newline is pinned so a Windows checkout and a Linux CI run produce
        # byte-identical files instead of a whole-file diff on every commit.
        try:
            destination.write_text(_normalise(content), encoding="utf-8", newline="\n")
        except OSError as exc:
            raise LessonGenerationError(f"Could not write {destination}: {exc}") from exc

        self.invalidate(subject)
        logger.debug("Wrote %s (%d bytes)", self.paths.relative(destination), destination.stat().st_size)
        return destination

    def invalidate(self, subject: str | None = None) -> None:
        """Drop cached listings for *subject*, or for everything if ``None``."""
        if subject is None:
            self._listing_cache.clear()
        else:
            self._listing_cache.pop(subject, None)


_TRAILING_WHITESPACE = re.compile(r"[ \t]+$", re.MULTILINE)
_EXCESS_BLANK_LINES = re.compile(r"\n{4,}")
_FENCE_WRAPPER = re.compile(r"^\s*```(?:markdown|md)?\s*\n(?P<body>.*?)\n\s*```\s*$", re.DOTALL)


def _normalise(content: str) -> str:
    """Tidy model output into a clean Markdown document.

    Models frequently wrap the whole answer in a ```markdown fence despite
    being told not to; that fence renders as a code block on GitHub and makes
    the lesson unreadable, so it is stripped when it encloses everything.
    """
    text = content.replace("\r\n", "\n").replace("\r", "\n").strip()

    fenced = _FENCE_WRAPPER.match(text)
    if fenced is not None:
        text = fenced.group("body").strip()

    text = _TRAILING_WHITESPACE.sub("", text)
    text = _EXCESS_BLANK_LINES.sub("\n\n\n", text)
    return text + "\n"
