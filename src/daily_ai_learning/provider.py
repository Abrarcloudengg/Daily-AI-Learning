"""OpenRouter chat-completion client.

Everything that can go wrong on a network call is handled in one place:
timeouts, connection resets, rate limits, upstream 5xx, HTML error pages served
instead of JSON, and well-formed responses that carry no content. Transient
failures are retried with exponential backoff and jitter; permanent ones fail
immediately with a message that says what to fix.

The API key is read from the environment at call time and never stored on an
object, logged, or included in an exception message.
"""

from __future__ import annotations

import os
import random
import time
from dataclasses import dataclass
from typing import Any, Callable

import requests

from .exceptions import ConfigurationError, ProviderError
from .logging_setup import get_logger
from .settings import API_KEY_ENV, Settings

__all__ = ["Completion", "OpenRouterClient", "resolve_api_key"]

logger = get_logger(__name__)

#: Status codes worth another attempt: rate limiting and upstream faults.
RETRYABLE_STATUS = frozenset({408, 409, 425, 429, 500, 502, 503, 504, 522, 524})

#: Status codes explaining what the operator must change.
_FATAL_HINTS: dict[int, str] = {
    400: "The request was rejected. The model name in config/settings.json may be wrong.",
    401: f"Authentication failed. Check that {API_KEY_ENV} holds a valid OpenRouter key.",
    402: "Your OpenRouter account is out of credit.",
    403: "Access denied. Your key may not be allowed to use this model.",
    404: "Endpoint or model not found. Check `api_url` and `model` in config/settings.json.",
    413: "The request was too large. Lower `max_tokens` in config/settings.json.",
}


@dataclass(frozen=True)
class Completion:
    """A successful model response."""

    content: str
    finish_reason: str | None
    model: str
    prompt_tokens: int | None = None
    completion_tokens: int | None = None

    @property
    def total_tokens(self) -> int | None:
        if self.prompt_tokens is None or self.completion_tokens is None:
            return None
        return self.prompt_tokens + self.completion_tokens


def resolve_api_key(env: dict[str, str] | None = None) -> str:
    """Return the OpenRouter API key from the environment.

    Raises:
        ConfigurationError: if the variable is missing or blank, with setup
            instructions for both local runs and GitHub Actions.
    """
    environ = os.environ if env is None else env
    key = (environ.get(API_KEY_ENV) or "").strip()

    if not key:
        raise ConfigurationError(
            f"{API_KEY_ENV} is not set.\n"
            f"  Local:  copy .env.example to .env and put your key in it.\n"
            f"  CI:     add it under Settings -> Secrets and variables -> Actions.\n"
            f"  Get a key at https://openrouter.ai/keys"
        )

    return key


class OpenRouterClient:
    """Minimal, resilient chat-completion client."""

    def __init__(
        self,
        settings: Settings,
        *,
        api_key: str | None = None,
        session: requests.Session | None = None,
        sleep: Callable[[float], None] = time.sleep,
    ) -> None:
        """
        Args:
            settings: Model, timeout, and retry configuration.
            api_key: Overrides the environment lookup. Intended for tests.
            session: Reused HTTP session. One is created if omitted.
            sleep: Injected so tests do not actually wait between retries.
        """
        self._settings = settings
        self._api_key = api_key or resolve_api_key()
        self._session = session or requests.Session()
        self._sleep = sleep

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def complete(self, system_prompt: str, user_prompt: str) -> Completion:
        """Send one chat completion request, retrying transient failures.

        Raises:
            ProviderError: on a permanent failure, or once every retry is spent.
        """
        payload = self._build_payload(system_prompt, user_prompt)
        last_error = "no attempt was made"

        for attempt in range(1, self._settings.max_retries + 1):
            logger.info("Requesting lesson from %s (attempt %d/%d)…", self._settings.model, attempt, self._settings.max_retries)

            try:
                response = self._session.post(
                    self._settings.api_url,
                    headers=self._headers(),
                    json=payload,
                    timeout=self._settings.request_timeout,
                )
            except requests.Timeout:
                last_error = f"request timed out after {self._settings.request_timeout:.0f}s"
                self._backoff(attempt, last_error)
                continue
            except requests.RequestException as exc:
                last_error = f"network error: {_redact(str(exc), self._api_key)}"
                self._backoff(attempt, last_error)
                continue

            if response.status_code in RETRYABLE_STATUS:
                last_error = f"provider returned HTTP {response.status_code}"
                self._backoff(attempt, last_error, retry_after=_retry_after(response))
                continue

            if response.status_code != 200:
                raise ProviderError(self._fatal_message(response))

            try:
                completion = self._parse(response.json())
            except ValueError:
                snippet = response.text[:200].replace("\n", " ")
                last_error = f"response was not JSON: {snippet!r}"
                self._backoff(attempt, last_error)
                continue
            except ProviderError as exc:
                last_error = str(exc)
                self._backoff(attempt, last_error)
                continue

            logger.info(
                "Received %d characters (finish_reason=%s, tokens=%s).",
                len(completion.content),
                completion.finish_reason,
                completion.total_tokens if completion.total_tokens is not None else "unknown",
            )
            return completion

        raise ProviderError(
            f"Gave up after {self._settings.max_retries} attempt(s). Last failure: {last_error}."
        )

    # ------------------------------------------------------------------
    # Internals
    # ------------------------------------------------------------------
    def _headers(self) -> dict[str, str]:
        return {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
            # Optional OpenRouter attribution headers.
            "HTTP-Referer": self._settings.referer,
            "X-Title": self._settings.app_title,
        }

    def _build_payload(self, system_prompt: str, user_prompt: str) -> dict[str, Any]:
        return {
            "model": self._settings.model,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            "temperature": self._settings.temperature,
            "max_tokens": self._settings.max_tokens,
        }

    def _parse(self, body: Any) -> Completion:
        """Turn a decoded JSON body into a :class:`Completion`."""
        if not isinstance(body, dict):
            raise ProviderError(f"Expected a JSON object, got {type(body).__name__}.")

        # OpenRouter reports upstream failures inside a 200 response.
        error = body.get("error")
        if isinstance(error, dict) and error:
            raise ProviderError(f"Provider error: {error.get('message', error)}")

        choices = body.get("choices")
        if not isinstance(choices, list) or not choices:
            raise ProviderError("Response contained no choices.")

        choice = choices[0]
        if not isinstance(choice, dict):
            raise ProviderError("Malformed choice in response.")

        message = choice.get("message")
        content = message.get("content") if isinstance(message, dict) else None

        if not isinstance(content, str) or not content.strip():
            raise ProviderError("Response contained an empty message.")

        usage = body.get("usage") if isinstance(body.get("usage"), dict) else {}

        return Completion(
            content=content,
            finish_reason=choice.get("finish_reason"),
            model=str(body.get("model") or self._settings.model),
            prompt_tokens=_as_int(usage.get("prompt_tokens")),
            completion_tokens=_as_int(usage.get("completion_tokens")),
        )

    def _fatal_message(self, response: requests.Response) -> str:
        hint = _FATAL_HINTS.get(response.status_code, "The request failed and cannot be retried.")
        detail = _redact(response.text[:300].replace("\n", " ").strip(), self._api_key)
        return f"HTTP {response.status_code} from the model provider. {hint}\n  Response: {detail}"

    def _backoff(self, attempt: int, reason: str, *, retry_after: float | None = None) -> None:
        """Log *reason* and sleep before the next attempt."""
        if attempt >= self._settings.max_retries:
            logger.warning("Attempt %d failed (%s); no attempts left.", attempt, reason)
            return

        if retry_after is not None:
            delay = min(retry_after, self._settings.retry_max_backoff)
        else:
            # Exponential backoff with jitter so parallel jobs do not retry in
            # lockstep and re-trigger the same rate limit.
            base = self._settings.retry_backoff * (2 ** (attempt - 1))
            delay = min(base, self._settings.retry_max_backoff) * random.uniform(0.6, 1.0)

        logger.warning("Attempt %d failed (%s); retrying in %.1fs.", attempt, reason, delay)
        self._sleep(delay)


def _retry_after(response: requests.Response) -> float | None:
    """Parse the ``Retry-After`` header, in seconds, if the provider sent one."""
    raw = response.headers.get("Retry-After")
    if not raw:
        return None
    try:
        return max(0.0, float(raw))
    except ValueError:
        return None


def _as_int(value: Any) -> int | None:
    return value if isinstance(value, int) else None


def _redact(text: str, secret: str) -> str:
    """Remove the API key from text that may be logged or raised."""
    if secret and secret in text:
        return text.replace(secret, "***redacted***")
    return text
