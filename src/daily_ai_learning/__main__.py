"""Allow ``python -m daily_ai_learning`` as an alternative to the console script."""

from __future__ import annotations

import sys

from .cli import main

if __name__ == "__main__":
    sys.exit(main())
