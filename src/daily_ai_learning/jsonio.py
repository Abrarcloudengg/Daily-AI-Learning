"""JSON helpers with atomic writes and actionable error messages.

``json.load`` failures used to surface as a raw ``JSONDecodeError`` naming
neither the file nor the fix. Worse, a plain ``open(..., "w")`` truncates the
target before the new content is serialised, so an interrupted run (a cancelled
GitHub Actions job, Ctrl-C, a full disk) could leave ``progress.json`` empty and
destroy the learning history. Both problems are solved here, once.
"""

from __future__ import annotations

import json
import os
import tempfile
from pathlib import Path
from typing import Any

from .exceptions import ConfigurationError

__all__ = ["read_json", "write_json"]


def read_json(path: Path, *, description: str = "JSON file") -> Any:
    """Read and parse *path*.

    Raises:
        ConfigurationError: if the file is missing, unreadable, or not valid
            JSON. The message always names the offending path.
    """
    try:
        text = path.read_text(encoding="utf-8")
    except FileNotFoundError as exc:
        raise ConfigurationError(f"{description} not found: {path}") from exc
    except OSError as exc:
        raise ConfigurationError(f"Cannot read {description} at {path}: {exc}") from exc

    try:
        return json.loads(text)
    except json.JSONDecodeError as exc:
        raise ConfigurationError(
            f"{description} at {path} is not valid JSON "
            f"(line {exc.lineno}, column {exc.colno}): {exc.msg}"
        ) from exc


def write_json(path: Path, payload: Any, *, indent: int = 4) -> None:
    """Serialise *payload* to *path* atomically.

    The content is written to a temporary file in the same directory, flushed
    to disk, and then moved into place with :func:`os.replace`, which is atomic
    on both POSIX and Windows. A crash mid-write leaves the previous file
    untouched rather than truncated.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    text = json.dumps(payload, indent=indent, ensure_ascii=False) + "\n"

    handle = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        newline="\n",
        dir=path.parent,
        prefix=f".{path.name}.",
        suffix=".tmp",
        delete=False,
    )
    temp_path = Path(handle.name)
    try:
        with handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp_path, path)
    except BaseException:
        temp_path.unlink(missing_ok=True)
        raise
