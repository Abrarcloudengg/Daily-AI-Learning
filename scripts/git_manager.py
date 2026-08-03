"""Deprecated compatibility layer for ``scripts/git_manager.py``.

Modern equivalent::

    from daily_ai_learning.git_ops import GitRepository
"""

from __future__ import annotations

import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parent.parent / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from daily_ai_learning.git_ops import GitRepository  # noqa: E402
from daily_ai_learning.paths import Paths  # noqa: E402
from daily_ai_learning.settings import Settings  # noqa: E402

__all__ = ["git_commit_and_push"]


def git_commit_and_push(day: int, topic: str) -> bool:
    """Sync, commit ``Day <day>: <topic>``, and push.

    Deprecated. Use :class:`daily_ai_learning.git_ops.GitRepository`.
    """
    paths = Paths.discover()
    repository = GitRepository(paths, Settings.load(paths))
    return repository.commit_and_push(f"Day {day}: {topic}")
