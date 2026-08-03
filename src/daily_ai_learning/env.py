"""Loading secrets from a local ``.env`` file.

``python-dotenv`` is used when it is installed. A small parser covering the
subset this project needs is kept as a fallback so a bare ``pip install
requests`` checkout still finds the API key instead of failing with a confusing
"key not set" message.

Values already present in the real environment always win: a shell export or a
GitHub Actions secret must never be silently overridden by a stale file.
"""

from __future__ import annotations

import os
from pathlib import Path

from .logging_setup import get_logger

__all__ = ["load_env_file"]

logger = get_logger(__name__)


def load_env_file(path: Path) -> int:
    """Load ``KEY=value`` pairs from *path* into ``os.environ``.

    Args:
        path: The ``.env`` file. A missing file is not an error — CI supplies
            secrets through the environment instead.

    Returns:
        How many variables were newly set.
    """
    if not path.is_file():
        return 0

    try:
        from dotenv import dotenv_values
    except ImportError:
        values = _parse(path)
    else:
        values = {k: v for k, v in dotenv_values(path, encoding="utf-8").items() if v is not None}

    applied = 0
    for key, value in values.items():
        if key in os.environ:
            continue
        os.environ[key] = value
        applied += 1

    if applied:
        logger.debug("Loaded %d variable(s) from %s.", applied, path.name)

    return applied


def _parse(path: Path) -> dict[str, str]:
    """Minimal ``.env`` parser: ``KEY=value``, ``#`` comments, optional quotes."""
    values: dict[str, str] = {}

    try:
        lines = path.read_text(encoding="utf-8").splitlines()
    except OSError as exc:
        logger.warning("Could not read %s: %s", path, exc)
        return values

    for raw in lines:
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue

        key, _, value = line.partition("=")
        key = key.removeprefix("export ").strip()
        value = value.strip()

        if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
            value = value[1:-1]

        if key:
            values[key] = value

    return values
