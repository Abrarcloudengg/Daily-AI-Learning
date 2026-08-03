"""Deprecated entry point kept for backwards compatibility.

``python scripts/generator.py`` still generates the next lesson, exactly as it
always did. It now delegates to the packaged CLI, so it gains retries, quality
gates, structured logging, and every other improvement automatically.

The modern equivalents::

    daily-ai generate                 # after `pip install -e .`
    python -m daily_ai_learning generate
"""

from __future__ import annotations

import sys
from pathlib import Path

_SRC = Path(__file__).resolve().parent.parent / "src"
if _SRC.is_dir() and str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))

from daily_ai_learning.cli import main  # noqa: E402


def run() -> int:
    """Generate the next lesson. Returns a process exit code."""
    argv = sys.argv[1:]

    # Preserve the old zero-argument behaviour while still allowing flags such
    # as `python scripts/generator.py --dry-run`.
    if not argv or argv[0].startswith("-"):
        argv = ["generate", *argv]

    return main(argv)


if __name__ == "__main__":
    sys.exit(run())
