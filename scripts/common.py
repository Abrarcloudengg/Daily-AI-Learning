"""Deprecated compatibility layer for ``scripts/common.py``.

The real implementations now live in the :mod:`daily_ai_learning` package. This
module re-exports the old names so existing snippets and muscle memory keep
working after the move to a ``src/`` layout.

Prefer the package directly::

    from daily_ai_learning.paths import Paths
    from daily_ai_learning.catalog import TopicCatalog
"""

from __future__ import annotations

import sys
import warnings
from pathlib import Path
from typing import Any

_SRC = Path(__file__).resolve().parent.parent / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from daily_ai_learning.catalog import TopicCatalog  # noqa: E402
from daily_ai_learning.jsonio import read_json, write_json  # noqa: E402
from daily_ai_learning.lessons import LessonLibrary  # noqa: E402
from daily_ai_learning.naming import (  # noqa: E402
    FOLDER_OVERRIDES,
    safe_topic_name,
    subject_slug,
)
from daily_ai_learning.paths import Paths  # noqa: E402
from daily_ai_learning.progress import Progress, ProgressStore  # noqa: E402

__all__ = [
    "BASE_DIR",
    "CONFIG_DIR",
    "FOLDER_OVERRIDES",
    "GENERATED_DIR",
    "PROGRESS_FILE",
    "README_FILE",
    "SUBJECTS_FILE",
    "lesson_dir",
    "lesson_exists",
    "load_json",
    "load_progress",
    "load_subjects",
    "load_topics",
    "reconcile_completed",
    "safe_topic_name",
    "save_json",
    "save_progress",
    "subject_slug",
    "topic_file",
]

PATHS = Paths.discover()
CATALOG = TopicCatalog(PATHS)
LIBRARY = LessonLibrary(PATHS)
STORE = ProgressStore(PATHS, CATALOG, LIBRARY)

# Legacy string constants, kept for callers that joined onto them.
BASE_DIR = str(PATHS.root)
CONFIG_DIR = str(PATHS.config_dir)
GENERATED_DIR = str(PATHS.generated_dir)
PROGRESS_FILE = str(PATHS.progress_file)
SUBJECTS_FILE = str(PATHS.subjects_file)
README_FILE = str(PATHS.readme_file)


def _deprecated(old: str, new: str) -> None:
    warnings.warn(
        f"scripts.common.{old}() is deprecated; use {new} instead.",
        DeprecationWarning,
        stacklevel=3,
    )


def load_json(path: str | Path) -> Any:
    """Deprecated. Use :func:`daily_ai_learning.jsonio.read_json`."""
    _deprecated("load_json", "daily_ai_learning.jsonio.read_json")
    return read_json(Path(path))


def save_json(path: str | Path, data: Any) -> None:
    """Deprecated. Use :func:`daily_ai_learning.jsonio.write_json`."""
    _deprecated("save_json", "daily_ai_learning.jsonio.write_json")
    write_json(Path(path), data)


def topic_file(subject: str) -> str:
    """Deprecated. Use ``Paths.topic_file``."""
    return str(PATHS.topic_file(subject))


def lesson_dir(subject: str) -> str:
    """Deprecated. Use ``Paths.lesson_dir``."""
    return str(PATHS.lesson_dir(subject))


def load_topics(subject: str) -> list[str] | None:
    """Deprecated. Use ``TopicCatalog.topics``.

    Returns ``None`` instead of raising, matching the old behaviour.
    """
    try:
        return CATALOG.topics(subject)
    except Exception:
        return None


def load_subjects() -> list[str]:
    """Deprecated. Use ``TopicCatalog.subjects``."""
    return CATALOG.subjects


def lesson_exists(subject: str, topic: str) -> bool:
    """Deprecated. Use ``LessonLibrary.exists``."""
    LIBRARY.invalidate(subject)
    return LIBRARY.exists(subject, topic)


def load_progress() -> dict[str, Any]:
    """Deprecated. Use ``ProgressStore.load``. Returns the legacy dict shape."""
    return STORE.load().to_dict()


def save_progress(progress: dict[str, Any]) -> None:
    """Deprecated. Use ``ProgressStore.save``."""
    write_json(PATHS.progress_file, progress)


def reconcile_completed(progress: dict[str, Any]) -> tuple[dict[str, Any], list[str]]:
    """Deprecated. Use ``ProgressStore.reconcile``."""
    record = Progress.from_dict(progress, default_subject=CATALOG.subjects[0])
    LIBRARY.invalidate()
    result = STORE.reconcile(record)
    return result.progress.to_dict(), result.dropped
