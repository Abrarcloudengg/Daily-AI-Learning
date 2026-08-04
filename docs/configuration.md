[← Docs home](index.md)

# Configuration

Settings come from three layers. Later layers win.

1. The defaults baked into `Settings`.
2. `config/settings.json` — checked in and reviewable.
3. `DAILY_AI_<FIELD>` environment variables — for a single run, or for CI.

The API key is deliberately *not* one of these. It is read from
`OPENROUTER_API_KEY` at the moment it is needed and is never stored on an
object that could end up in a traceback.

## `config/settings.json`

### Model provider

| Key | Default | Notes |
| --- | --- | --- |
| `model` | `qwen/qwen3-coder` | Any [OpenRouter model slug](https://openrouter.ai/models). Free tiers work. |
| `api_url` | `https://openrouter.ai/api/v1/chat/completions` | Must be `https://`. Plain `http` is rejected — it would send your key in clear text. |
| `temperature` | `0.7` | 0.0–2.0. Lower is more consistent, higher is more varied. |
| `max_tokens` | `8000` | Must be ≥ 1000. The 24-section lesson template does not fit in less, and every lesson would come back truncated. |

### Resilience

| Key | Default | Notes |
| --- | --- | --- |
| `request_timeout` | `180.0` | Seconds. Long lessons on a slow free-tier model genuinely take this long. |
| `max_retries` | `3` | Total attempts, not extra attempts. |
| `retry_backoff` | `5.0` | Base delay in seconds. Doubles each attempt, with jitter. |
| `retry_max_backoff` | `60.0` | Ceiling on a single wait. A `Retry-After` header always wins over the computed delay. |

### Quality gates

| Key | Default | Notes |
| --- | --- | --- |
| `min_lesson_chars` | `1200` | Anything shorter is treated as a truncated response and rejected, not saved. |
| `require_all_sections` | `false` | Set `true` to also reject a lesson that is missing any of the 24 template sections. Strict, and occasionally too strict. |

### Run behaviour

| Key | Default | Notes |
| --- | --- | --- |
| `lessons_per_run` | `1` | The default for `daily-ai generate`. `--count` overrides it. |
| `log_level` | `INFO` | `DEBUG`, `INFO`, `WARNING`, `ERROR`, or `CRITICAL`. |

### Git

| Key | Default | Notes |
| --- | --- | --- |
| `git_remote` | `origin` | |
| `git_branch` | `main` | |

### Attribution

| Key | Default | Notes |
| --- | --- | --- |
| `referer` | the repository URL | Sent as `HTTP-Referer`. OpenRouter uses it for their app leaderboard. The README generator also parses the owner and repository name out of it for badges. |
| `app_title` | `Daily-AI-Learning` | Sent as `X-Title`. |

## Environment overrides

Every key above has an override named `DAILY_AI_` plus the key in upper case:

```bash
DAILY_AI_MODEL=anthropic/claude-3.5-sonnet daily-ai generate
DAILY_AI_MAX_TOKENS=12000 DAILY_AI_LOG_LEVEL=DEBUG daily-ai generate
DAILY_AI_LESSONS_PER_RUN=3 daily-ai generate
```

Values are coerced to the declared type. `DAILY_AI_MAX_TOKENS=lots` fails
immediately with a readable message rather than deep inside an HTTP call.

An unknown key in `settings.json` is a hard error listing the valid keys — a
typo like `"max_token"` should not silently do nothing.

## The `.env` file

`.env` is loaded before settings are read. Real environment variables always
beat the file, so CI secrets are never shadowed by a stale local file.

```ini
OPENROUTER_API_KEY=sk-or-v1-...

# Optional single-run overrides
# DAILY_AI_MODEL=qwen/qwen3-coder
# DAILY_AI_LOG_LEVEL=DEBUG
```

`.env` is gitignored, and `daily-ai doctor` fails if it is ever tracked.

## Workspace root

Paths are resolved from a discovered root, not from the current directory, so
commands work from anywhere:

1. `$DAILY_AI_ROOT` if it is set.
2. Otherwise the nearest ancestor containing `pyproject.toml`,
   `config/subjects.json`, or `.git`.
3. Otherwise the current directory.

`--root PATH` overrides all of it. Tests use this to run against a temporary
directory.
