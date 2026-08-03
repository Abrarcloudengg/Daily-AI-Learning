"""Runtime configuration.

Values come from three layers, later layers overriding earlier ones:

1. The defaults on :class:`Settings`.
2. ``config/settings.json`` — checked in, reviewable, the place to change the
   model or token budget without touching code.
3. ``DAILY_AI_*`` environment variables — the escape hatch for a single run or
   for CI, where editing a file is awkward.

The API key deliberately lives outside this object. It is read from the
environment at the moment it is needed and never stored on a dataclass that
might end up in a log line or a traceback.
"""

from __future__ import annotations

import os
from dataclasses import dataclass, fields
from typing import Any, Final

from .exceptions import ConfigurationError
from .jsonio import read_json
from .paths import Paths

__all__ = ["API_KEY_ENV", "Settings"]

#: Environment variable holding the OpenRouter API key.
API_KEY_ENV: Final = "OPENROUTER_API_KEY"

#: Prefix for per-setting environment overrides, e.g. ``DAILY_AI_MODEL``.
_ENV_PREFIX: Final = "DAILY_AI_"


@dataclass(frozen=True)
class Settings:
    """Tunable knobs for a generation run."""

    # -- Model provider -------------------------------------------------
    model: str = "qwen/qwen3-coder"
    api_url: str = "https://openrouter.ai/api/v1/chat/completions"
    temperature: float = 0.7
    max_tokens: int = 8000

    # -- Resilience -----------------------------------------------------
    request_timeout: float = 180.0
    max_retries: int = 3
    retry_backoff: float = 5.0
    retry_max_backoff: float = 60.0

    # -- Quality gates --------------------------------------------------
    min_lesson_chars: int = 1200
    require_all_sections: bool = False

    # -- Run behaviour --------------------------------------------------
    lessons_per_run: int = 1
    log_level: str = "INFO"

    # -- Git ------------------------------------------------------------
    git_remote: str = "origin"
    git_branch: str = "main"

    # -- Attribution sent to OpenRouter (used for their leaderboards) ----
    referer: str = "https://github.com/Abrarcloudengg/Daily-AI-Learning"
    app_title: str = "Daily-AI-Learning"

    # ------------------------------------------------------------------
    # Loading
    # ------------------------------------------------------------------
    @classmethod
    def load(cls, paths: Paths | None = None, *, env: dict[str, str] | None = None) -> Settings:
        """Build settings from ``config/settings.json`` plus environment overrides."""
        paths = paths or Paths.discover()
        environ = os.environ if env is None else env

        values: dict[str, Any] = {}

        if paths.settings_file.exists():
            raw = read_json(paths.settings_file, description="settings file")
            if not isinstance(raw, dict):
                raise ConfigurationError(
                    f"{paths.settings_file} must contain a JSON object, got {type(raw).__name__}."
                )
            known = {field.name for field in fields(cls)}
            unknown = sorted(set(raw) - known)
            if unknown:
                raise ConfigurationError(
                    f"Unknown key(s) in {paths.settings_file}: {', '.join(unknown)}. "
                    f"Valid keys: {', '.join(sorted(known))}."
                )
            values.update(raw)

        values.update(cls._env_overrides(environ))

        try:
            settings = cls(**values)
        except TypeError as exc:  # pragma: no cover - guarded by the check above
            raise ConfigurationError(f"Invalid settings: {exc}") from exc

        settings.validate()
        return settings

    @classmethod
    def _env_overrides(cls, environ: dict[str, str]) -> dict[str, Any]:
        """Collect ``DAILY_AI_<FIELD>`` variables, coerced to the field type."""
        overrides: dict[str, Any] = {}

        for field in fields(cls):
            raw = environ.get(f"{_ENV_PREFIX}{field.name.upper()}")
            if raw is None:
                continue
            overrides[field.name] = _coerce(field.name, raw, field.type)

        return overrides

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------
    def validate(self) -> None:
        """Reject values that would fail later in a confusing way.

        Raises:
            ConfigurationError: on the first invalid value found.
        """
        if not self.model.strip():
            raise ConfigurationError("`model` must not be empty.")

        if not self.api_url.startswith("https://"):
            raise ConfigurationError(
                f"`api_url` must be an https:// URL, got {self.api_url!r}. "
                "Plain http would send the API key in clear text."
            )

        if not 0.0 <= self.temperature <= 2.0:
            raise ConfigurationError(f"`temperature` must be within 0.0-2.0, got {self.temperature}.")

        if self.max_tokens < 1000:
            raise ConfigurationError(
                f"`max_tokens` must be at least 1000, got {self.max_tokens}. "
                "The lesson template cannot fit in less and every lesson would be truncated."
            )

        for name in ("request_timeout", "retry_backoff", "retry_max_backoff", "min_lesson_chars"):
            if getattr(self, name) <= 0:
                raise ConfigurationError(f"`{name}` must be positive, got {getattr(self, name)}.")

        if self.max_retries < 1:
            raise ConfigurationError(f"`max_retries` must be at least 1, got {self.max_retries}.")

        if self.lessons_per_run < 1:
            raise ConfigurationError(f"`lessons_per_run` must be at least 1, got {self.lessons_per_run}.")

        if self.log_level.upper() not in {"DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"}:
            raise ConfigurationError(f"`log_level` is not a valid level: {self.log_level!r}.")

        if not self.git_remote.strip() or not self.git_branch.strip():
            raise ConfigurationError("`git_remote` and `git_branch` must not be empty.")


def _coerce(name: str, raw: str, annotation: Any) -> Any:
    """Convert an environment string to the type declared on the dataclass."""
    text = str(annotation)

    try:
        if "bool" in text:
            lowered = raw.strip().lower()
            if lowered in {"1", "true", "yes", "on"}:
                return True
            if lowered in {"0", "false", "no", "off"}:
                return False
            raise ValueError(f"expected a boolean, got {raw!r}")
        if "int" in text:
            return int(raw)
        if "float" in text:
            return float(raw)
    except ValueError as exc:
        raise ConfigurationError(f"{_ENV_PREFIX}{name.upper()}={raw!r} is invalid: {exc}") from exc

    return raw
