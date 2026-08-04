# Changelog

All notable changes to this project are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

Nothing yet.

## [2.0.0] - 2026-08-04

A full rewrite of the internals. The daily automation behaves the same from the
outside, but nothing underneath it is the same.

### Added

- **Installable package** `daily_ai_learning` under `src/`, with a `daily-ai`
  console entry point, `python -m daily_ai_learning` support, and a PEP 561
  `py.typed` marker.
- **CLI with real subcommands**: `generate`, `next`, `status`, `readme`,
  `validate`, `doctor`, `version`. Bare `daily-ai` still means `generate`.
- **`daily-ai doctor`** — checks the Python version, workspace layout,
  settings, API key, curriculum integrity, git availability, lesson count, and
  whether `.env` has accidentally been committed.
- **`daily-ai validate`** — catches duplicate subjects, subjects whose slugs
  collide, a topic file whose declared `subject` disagrees with
  `subjects.json`, two subjects sharing an identical topic list, and subjects
  with suspiciously few topics.
- **`config/settings.json`** — model, temperature, token budget, timeouts,
  retry policy, quality thresholds, log level, and git remote/branch are now
  configuration instead of literals scattered through the code. Every key can be
  overridden for a single run with a `DAILY_AI_<KEY>` environment variable.
- **Retry with exponential backoff and jitter** for the OpenRouter call, which
  honours the `Retry-After` header, retries the statuses worth retrying, and
  fails immediately on the ones that will never succeed (401, 402, 404, …) with
  an actionable message instead of a stack trace.
- **Quality gate on generated lessons** — a lesson that was truncated
  mid-generation, came back too short, or has an unbalanced code fence is
  rejected instead of being written to disk and marked complete.
- **Atomic writes** for `progress.json` and every lesson file: write to a
  temporary file, `fsync`, then `os.replace`. A crash or a cancelled Actions run
  can no longer leave a half-written file behind.
- **Filesystem reconciliation** — `progress.json` is treated as a cache, not as
  the truth. On every run the completed list is rebuilt from what is actually in
  `generated/`, so a merge conflict or a manual deletion self-heals.
- **`--dry-run`** shows exactly what would be generated without an API call,
  without writing a file, and without touching progress.
- **`--count N`** generates several lessons in one run, with a single commit.
- **Structured logging** to stderr with an optional `--log-file`, and a
  timestamped verbose format when running under GitHub Actions.
- **Typed exception hierarchy** mapped to sysexits-style exit codes: 65 bad
  data, 69 provider unavailable, 70 generation failed, 78 configuration,
  130 interrupted.
- **Test suite** covering naming, path discovery, atomic JSON writes, catalog
  validation, progress reconciliation, subject transitions, lesson quality
  inspection, provider retry behaviour against a fake HTTP session, README
  rendering, and the CLI end to end.
- **CI** on Python 3.10–3.13 plus a Windows leg, running ruff, ruff format,
  mypy, pytest with coverage, and an offline end-to-end smoke test that also
  verifies `README.md` is reproducible.
- **Release workflow** that refuses to publish when the git tag disagrees with
  the version in `pyproject.toml`, builds an sdist and a wheel, and attaches the
  matching CHANGELOG section.
- **GitHub Pages** documentation site under `docs/`.
- Community files: `LICENSE` (MIT), `CONTRIBUTING.md`, `SECURITY.md`,
  `CODE_OF_CONDUCT.md`, issue templates, a pull request template, and
  `dependabot.yml`.

### Changed

- **README is now generated**, not maintained by hand — dashboard, per-subject
  progress bars, architecture and workflow diagrams, badges, FAQ, and roadmap
  all come from `daily-ai readme`.
- Topic files moved from `config/*.json` to `config/topics/*.json`. The old flat
  location is still read as a fallback, so an existing checkout keeps working.
- `scripts/generator.py`, `scripts/topic_selector.py`,
  `scripts/readme_updater.py`, `scripts/git_manager.py`, and
  `scripts/common.py` are now thin shims that delegate to the package. Their
  public functions keep the same names and signatures and emit a
  `DeprecationWarning`.
- The daily workflow checks that `OPENROUTER_API_KEY` exists before spending
  three minutes discovering it does not, stages only the paths it is allowed to
  change instead of `git add -A`, and retries the push up to three times behind
  a rebase.

### Fixed

- **`config/dsa_topics.json` was a byte-for-byte copy of the Node.js topic
  list**, declaring `"subject": "Node.js"`. Left alone it would have generated
  an entire Node.js course into `generated/DSA/`. Replaced with a real 66-topic
  DSA roadmap, and `daily-ai validate` now fails on any repeat of this mistake.
- **Two competing day counters** could disagree after any interruption. There is
  now one derived counter: `day == len(completed) + 1`.
- **Double commit under GitHub Actions** — the pipeline committed, then the
  workflow committed again. The pipeline now detects CI and leaves git to the
  workflow.
- **`shell=True` in the git helper**, which made every command a potential
  injection point through a topic name.
- **O(n²) directory listing** — the generator called `os.listdir` once per topic
  per run. Listings are cached per subject.
- **Relative paths** meant the scripts only worked when invoked from the
  repository root. Paths are now discovered from a marker file, or from
  `$DAILY_AI_ROOT`.
- **`KeyError` on a malformed `progress.json`** — every read is tolerant and
  falls back to a rebuilt record.
- **Unicode crash on Windows** when a lesson containing an emoji was logged to a
  cp1252 console. The console stream is reconfigured to UTF-8 with replacement.
- A lesson wrapped by the model in a whole-document ```` ```markdown ```` fence
  is unwrapped before it is written.
- Progress is written **after** the lesson file, not before, so an interrupted
  run can never mark a topic complete without the lesson existing.

### Security

- The API key is never stored on an object, never logged, and is redacted from
  any provider error text before it reaches a log record.
- `daily-ai doctor` fails if `.env` is tracked by git.
- `.gitignore` now covers `*.egg-info/`, tooling caches, and `logs/`.

## [1.0.0] - 2025

Initial version: a set of scripts under `scripts/` driven by a single GitHub
Actions workflow, generating one lesson a day into `generated/`.

[Unreleased]: https://github.com/Abrarcloudengg/Daily-AI-Learning/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/Abrarcloudengg/Daily-AI-Learning/releases/tag/v2.0.0
[1.0.0]: https://github.com/Abrarcloudengg/Daily-AI-Learning/releases/tag/v1.0.0
