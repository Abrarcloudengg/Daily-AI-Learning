[← Docs home](index.md)

# CLI reference

```
daily-ai [--version] <command> [options]
```

Three equivalent entry points:

```bash
daily-ai generate                 # installed console script
python -m daily_ai_learning generate
python scripts/generator.py       # legacy shim, still supported
```

A bare `daily-ai` means `daily-ai generate`.

## Global options

Available on every command.

| Option | Meaning |
| --- | --- |
| `--root PATH` | Workspace root. Defaults to `$DAILY_AI_ROOT`, otherwise the enclosing repository. |
| `--log-level {DEBUG,INFO,WARNING,ERROR}` | Console verbosity. Overrides `log_level` in settings. |
| `--log-file PATH` | Also write a DEBUG-level log to this file. |

Human-readable output goes to **stderr**. Only machine-readable output — right
now just `status --commit-message` — goes to stdout, so you can pipe it safely.

## `generate`

Generate the next lesson (or several), update the README, and commit.

| Option | Meaning |
| --- | --- |
| `-n N`, `--count N` | Number of lessons. Defaults to `lessons_per_run`. |
| `--dry-run` | Show what would be generated. No API call, no file written, no progress change. |
| `--no-git` | Write the lesson but do not commit or push. |

```bash
daily-ai generate
daily-ai generate --count 3
daily-ai generate --dry-run
daily-ai generate --no-git --log-level DEBUG
```

Under GitHub Actions the pipeline never commits, even without `--no-git` — the
workflow owns that step, and doing it in both places produced two commits per
lesson in v1.

## `next`

Print the topic that would be generated next. No API call, no writes.

```bash
$ daily-ai next
Next up: Day 13 · Python · 13/45 · Dictionaries
```

## `status`

Progress dashboard.

| Option | Meaning |
| --- | --- |
| `--commit-message` | Print only a one-line commit message to stdout. Used by the daily workflow. |

```bash
$ daily-ai status
Daily AI Learning 2.0.0
Workspace: /home/you/Daily-AI-Learning

  Subject        Python
  Last topic     Dictionaries
  Next lesson    Day 13
  Overall        12/740 topics (1.62%)
  Subjects done  0/15
  Files on disk  12

  ▶ Python          12/45
    JavaScript       0/45
    ...
```

If `progress.json` disagreed with what is on disk, `status` says so and repairs
it in memory. `daily-ai readme` persists the repair.

## `readme`

Re-render `README.md` from the current progress. Costs nothing, calls nothing.

The README is generated output — edit `src/daily_ai_learning/readme.py`, not the
file. CI fails if re-rendering produces a diff.

## `validate`

Check every configuration file. Run this after editing the curriculum.

Catches:

- a subject in `subjects.json` with no topic file
- a topic file whose declared `subject` disagrees with `subjects.json`
- duplicate subjects, or two subjects whose slugs collide
- **two subjects with an identical topic list** — this is the check that would
  have caught `dsa_topics.json` being a copy of `nodejs_topics.json`
- a subject with fewer than five topics

Exit code 65 on errors, 0 on warnings only.

## `doctor`

Diagnose the environment before a run: Python version, workspace layout,
settings, API key presence, curriculum integrity, git availability, lesson
count, whether `.env` has leaked into git, and whether you are in CI.

Never prints the key itself — only whether one was found.

Exit code 78 if any check fails.

## `version`

Version, Python, resolved workspace root, and configured model.

## Exit codes

Chosen so that a CI step can tell "the model was busy" apart from "your
configuration is wrong".

| Code | Name | Meaning |
| --- | --- | --- |
| `0` | — | Success. Includes "the roadmap is finished". |
| `65` | `DATAERR` | Bad curriculum or progress data. |
| `69` | `UNAVAILABLE` | The provider failed after every retry. |
| `70` | `SOFTWARE` | Generation or a git operation failed. |
| `78` | `CONFIG` | Missing API key, invalid settings, failed `doctor`. |
| `130` | — | Interrupted with Ctrl-C. Nothing left half-written. |
