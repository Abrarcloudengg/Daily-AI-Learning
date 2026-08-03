"""Logging configuration.

The old scripts communicated exclusively through ``print``. That made output
impossible to filter, impossible to timestamp, and — on Windows — fatal: the
default ``cp1252`` console encoding cannot represent the emoji in the status
messages, so a ``UnicodeEncodeError`` killed runs that were otherwise fine.

This module fixes both: real logging with levels and timestamps, plus a stream
that degrades gracefully instead of crashing when the terminal cannot render a
character.
"""

from __future__ import annotations

import logging
import os
import sys
from pathlib import Path
from typing import IO, Any, ClassVar

__all__ = ["configure_logging", "get_logger"]

_CONSOLE_FORMAT = "%(message)s"
_VERBOSE_FORMAT = "%(asctime)s %(levelname)-8s %(name)s: %(message)s"
_FILE_FORMAT = "%(asctime)s %(levelname)-8s %(name)s: %(message)s"

_configured = False


class _LevelPrefixFormatter(logging.Formatter):
    """Prefix console records with a glyph so severity is visible at a glance."""

    _PREFIXES: ClassVar[dict[int, str]] = {
        logging.DEBUG: "·",
        logging.INFO: "",
        logging.WARNING: "warning:",
        logging.ERROR: "error:",
        logging.CRITICAL: "fatal:",
    }

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        prefix = self._PREFIXES.get(record.levelno, "")
        return f"{prefix} {message}" if prefix else message


def _make_console_stream(stream: IO[str]) -> IO[str]:
    """Return *stream* reconfigured to UTF-8 with replacement on failure.

    Reconfiguration is best effort: a stream that has been redirected to a
    pipe, captured by pytest, or replaced by a custom object may not support
    it, and that is not an error worth failing a run over.
    """
    reconfigure = getattr(stream, "reconfigure", None)
    if callable(reconfigure):
        try:
            reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass
    return stream


def configure_logging(
    level: str | int = "INFO",
    *,
    log_file: Path | None = None,
    verbose_console: bool | None = None,
    force: bool = False,
) -> logging.Logger:
    """Install handlers on the package logger and return it.

    Args:
        level: Threshold for the console handler.
        log_file: Optional path receiving an unfiltered DEBUG-level copy. The
            parent directory is created if needed; a failure to open it is
            reported once and never aborts the run.
        verbose_console: Include timestamps and logger names on the console.
            Defaults to on under CI, where interleaved output needs anchoring.
        force: Reinstall handlers even if this function already ran. Used by
            tests; ordinary callers should leave it alone.

    Returns:
        The configured ``daily_ai_learning`` logger.
    """
    global _configured

    logger = logging.getLogger("daily_ai_learning")

    if _configured and not force:
        return logger

    for handler in list(logger.handlers):
        logger.removeHandler(handler)
        handler.close()

    logger.setLevel(logging.DEBUG)
    logger.propagate = False

    if verbose_console is None:
        verbose_console = os.getenv("GITHUB_ACTIONS") == "true"

    console = logging.StreamHandler(_make_console_stream(sys.stderr))
    console.setLevel(_normalise_level(level))
    console.setFormatter(
        logging.Formatter(_VERBOSE_FORMAT)
        if verbose_console
        else _LevelPrefixFormatter(_CONSOLE_FORMAT)
    )
    logger.addHandler(console)

    if log_file is not None:
        try:
            log_file.parent.mkdir(parents=True, exist_ok=True)
            file_handler = logging.FileHandler(log_file, encoding="utf-8")
        except OSError as exc:
            logger.warning("Could not open log file %s: %s", log_file, exc)
        else:
            file_handler.setLevel(logging.DEBUG)
            file_handler.setFormatter(logging.Formatter(_FILE_FORMAT))
            logger.addHandler(file_handler)

    _configured = True
    return logger


def get_logger(name: str) -> logging.Logger:
    """Return a child logger of the package logger.

    Args:
        name: Usually ``__name__``. The package prefix is stripped so log lines
            read ``pipeline: ...`` rather than the full dotted path.
    """
    short = name.rsplit(".", 1)[-1]
    return logging.getLogger(f"daily_ai_learning.{short}")


def _normalise_level(level: str | int) -> int:
    if isinstance(level, int):
        return level
    resolved: Any = logging.getLevelName(str(level).upper())
    return resolved if isinstance(resolved, int) else logging.INFO
