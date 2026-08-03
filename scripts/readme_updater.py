"""Deprecated compatibility layer for ``scripts/readme_updater.py``.

Modern equivalent::

    daily-ai readme
    # or: from daily_ai_learning.readme import ReadmeRenderer
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
from daily_ai_learning.readme import ReadmeRenderer  # noqa: E402
from daily_ai_learning.settings import Settings  # noqa: E402

__all__ = ["update_readme"]


def update_readme() -> None:
    """Regenerate ``README.md`` from the current progress and catalogue."""
    paths = Paths.discover()
    catalog = TopicCatalog(paths)
    library = LessonLibrary(paths)
    store = ProgressStore(paths, catalog, library)
    settings = Settings.load(paths)

    ReadmeRenderer(paths, catalog, store, settings, library).write(store.load())


if __name__ == "__main__":
    from daily_ai_learning.cli import main

    sys.exit(main(["readme"]))
