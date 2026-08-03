"""Deprecated compatibility layer for ``scripts/topic_selector.py``.

Modern equivalent::

    from daily_ai_learning.selector import TopicSelector
"""

from __future__ import annotations

import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parent.parent / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from daily_ai_learning.catalog import TopicCatalog  # noqa: E402
from daily_ai_learning.lessons import LessonLibrary  # noqa: E402
from daily_ai_learning.paths import Paths  # noqa: E402
from daily_ai_learning.progress import ProgressStore  # noqa: E402
from daily_ai_learning.selector import TopicSelector  # noqa: E402

__all__ = ["get_next_topic"]


def get_next_topic() -> tuple[str | None, str | None]:
    """Return ``(subject, topic)`` for the next lesson, or ``(None, None)``.

    Deprecated. Use :class:`daily_ai_learning.selector.TopicSelector`, which
    also reports the day number and the position within the subject.
    """
    paths = Paths.discover()
    catalog = TopicCatalog(paths)
    library = LessonLibrary(paths)
    store = ProgressStore(paths, catalog, library)

    progress = store.load()
    selection = TopicSelector(paths, catalog, library, store).select(progress)
    store.save(progress)

    if selection is None:
        return None, None

    return selection.subject, selection.topic


if __name__ == "__main__":
    from daily_ai_learning.cli import main

    sys.exit(main(["next"]))
