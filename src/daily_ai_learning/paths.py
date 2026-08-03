"""Filesystem layout of a Daily AI Learning workspace.

Every path the project touches is derived from a single :class:`Paths` value.
Nothing in the codebase builds a path relative to the current working
directory, so ``python scripts/generator.py``, ``daily-ai generate``, and a
pytest run inside ``tmp_path`` all resolve identically.
"""

from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from .naming import lesson_folder_name, topic_filename

__all__ = ["ENV_ROOT", "Paths"]

#: Environment variable that pins the workspace root, used by tests and by
#: anyone running the CLI against a checkout other than the installed one.
ENV_ROOT = "DAILY_AI_ROOT"

#: A directory is recognised as a workspace root when it contains any of these.
_ROOT_MARKERS = ("pyproject.toml", "config/subjects.json", ".git")


@dataclass(frozen=True)
class Paths:
    """Resolved locations of every directory and file the project uses."""

    root: Path

    def __post_init__(self) -> None:
        # Normalise once so equality and logging are predictable.
        object.__setattr__(self, "root", Path(self.root).expanduser().resolve())

    # ------------------------------------------------------------------
    # Discovery
    # ------------------------------------------------------------------
    @classmethod
    def discover(cls, start: Path | str | None = None) -> Paths:
        """Locate the workspace root.

        Resolution order:

        1. ``$DAILY_AI_ROOT`` when set — an explicit override always wins.
        2. The nearest ancestor of *start* (or of this module) containing a
           root marker.
        3. The current working directory, as a last resort.
        """
        override = os.getenv(ENV_ROOT)
        if override:
            return cls(Path(override))

        origin = Path(start) if start is not None else Path(__file__).resolve()
        if origin.is_file():
            origin = origin.parent

        for candidate in (origin, *origin.parents):
            if any((candidate / marker).exists() for marker in _ROOT_MARKERS):
                return cls(candidate)

        return cls(Path.cwd())

    # ------------------------------------------------------------------
    # Directories
    # ------------------------------------------------------------------
    @property
    def config_dir(self) -> Path:
        """Curriculum and runtime configuration."""
        return self.root / "config"

    @property
    def topics_dir(self) -> Path:
        """Preferred home for per-subject topic files."""
        return self.config_dir / "topics"

    @property
    def data_dir(self) -> Path:
        """Generated state that the pipeline owns."""
        return self.root / "data"

    @property
    def generated_dir(self) -> Path:
        """Root of the lesson library, one subdirectory per subject."""
        return self.root / "generated"

    @property
    def logs_dir(self) -> Path:
        """Rotating run logs. Ignored by git."""
        return self.root / "logs"

    @property
    def docs_dir(self) -> Path:
        """Sources for the GitHub Pages site."""
        return self.root / "docs"

    # ------------------------------------------------------------------
    # Files
    # ------------------------------------------------------------------
    @property
    def subjects_file(self) -> Path:
        return self.config_dir / "subjects.json"

    @property
    def settings_file(self) -> Path:
        return self.config_dir / "settings.json"

    @property
    def progress_file(self) -> Path:
        return self.data_dir / "progress.json"

    @property
    def readme_file(self) -> Path:
        return self.root / "README.md"

    @property
    def env_file(self) -> Path:
        return self.root / ".env"

    # ------------------------------------------------------------------
    # Derived paths
    # ------------------------------------------------------------------
    def topic_file(self, subject: str) -> Path:
        """Return the topic file for *subject*.

        ``config/topics/<slug>_topics.json`` is preferred. The flat legacy
        location ``config/<slug>_topics.json`` is still honoured so an existing
        checkout keeps working after upgrading without moving any files.
        """
        name = topic_filename(subject)
        preferred = self.topics_dir / name
        if preferred.exists():
            return preferred

        legacy = self.config_dir / name
        if legacy.exists():
            return legacy

        # Neither exists: report the preferred location in the error message.
        return preferred

    def lesson_dir(self, subject: str) -> Path:
        """Return the directory holding *subject*'s generated lessons."""
        return self.generated_dir / lesson_folder_name(subject)

    def relative(self, path: Path) -> str:
        """Return *path* relative to the workspace root, for readable logs."""
        try:
            return path.resolve().relative_to(self.root).as_posix()
        except ValueError:
            return str(path)
