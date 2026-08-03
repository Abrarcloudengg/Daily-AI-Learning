"""Exception hierarchy for the project.

Every failure raised on purpose derives from :class:`DailyAILearningError`, so
the CLI can catch one base class, print a readable message, and exit with a
meaningful status code instead of dumping a traceback at users.
"""

from __future__ import annotations

__all__ = [
    "ConfigurationError",
    "CurriculumError",
    "DailyAILearningError",
    "GitOperationError",
    "LessonGenerationError",
    "ProgressError",
    "ProviderError",
]


class DailyAILearningError(Exception):
    """Base class for every error this project raises deliberately."""

    #: Process exit code used when the CLI terminates because of this error.
    exit_code: int = 1


class ConfigurationError(DailyAILearningError):
    """Settings or environment values are missing, malformed, or unusable."""

    exit_code = 78  # EX_CONFIG


class CurriculumError(DailyAILearningError):
    """The subject list or a topic file is missing or structurally invalid."""

    exit_code = 65  # EX_DATAERR


class ProgressError(DailyAILearningError):
    """``data/progress.json`` could not be read, parsed, or written."""

    exit_code = 65  # EX_DATAERR


class ProviderError(DailyAILearningError):
    """The upstream model provider failed after every retry was exhausted."""

    exit_code = 69  # EX_UNAVAILABLE


class LessonGenerationError(DailyAILearningError):
    """A lesson was returned but is empty, truncated, or missing sections."""

    exit_code = 70  # EX_SOFTWARE


class GitOperationError(DailyAILearningError):
    """A git command failed in a way the pipeline cannot recover from."""

    exit_code = 70  # EX_SOFTWARE
