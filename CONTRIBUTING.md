# Contributing

Thanks for looking. This project is small enough that a good pull request can
land the same day.

## Quick start

```bash
git clone https://github.com/Abrarcloudengg/Daily-AI-Learning.git
cd Daily-AI-Learning

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

python -m pip install -e ".[dev]"

cp .env.example .env              # Windows: copy .env.example .env
# put your OpenRouter key in .env

daily-ai doctor                   # every check should be green
```

You do **not** need an API key to work on most of the codebase. Everything
except `daily-ai generate` runs offline:

```bash
daily-ai validate      # check the curriculum files
daily-ai next          # what would be generated next
daily-ai status        # progress dashboard
daily-ai readme        # re-render README.md
daily-ai generate --dry-run --no-git
```

## Before you open a pull request

```bash
python -m ruff check src tests scripts
python -m ruff format src tests scripts
python -m mypy src
python -m pytest
```

CI runs exactly these, on Python 3.10–3.13 plus one Windows leg. If they pass
locally they will pass there.

Two extra rules CI enforces that are easy to miss:

- **`README.md` is generated.** Do not hand-edit it. Change
  `src/daily_ai_learning/readme.py`, run `daily-ai readme`, and commit the
  result. CI fails if re-rendering produces a diff.
- **`scripts/*.py` are compatibility shims.** They exist so old commands and
  old blog links keep working. Add features to `src/daily_ai_learning/`, not
  there.

## Good first contributions

| Kind | Where | Notes |
| --- | --- | --- |
| Add or fix curriculum topics | `config/topics/*.json` | Keep topics ordered beginner → advanced. Run `daily-ai validate`. |
| Add a whole new subject | `config/subjects.json` + `config/topics/<slug>_topics.json` | The slug is the lowercased subject with non-alphanumerics stripped. |
| Improve lesson quality | `src/daily_ai_learning/prompts.py` | Include a before/after sample in the PR. |
| Better README output | `src/daily_ai_learning/readme.py` | Attach a screenshot. |
| Tests | `tests/` | Always welcome, no discussion needed. |

## Adding a subject, end to end

1. Append the subject name to `config/subjects.json`.
2. Create `config/topics/<slug>_topics.json`:

   ```json
   {
     "subject": "Rust",
     "topics": ["Introduction to Rust", "Installing Rust", "..."]
   }
   ```

   The `subject` field must match `subjects.json` exactly.
3. If the name is not a legal folder name on Windows, add an entry to
   `FOLDER_OVERRIDES` in `src/daily_ai_learning/naming.py` — that is why
   `Node.js` lands in `generated/NodeJS/`.
4. `daily-ai validate` must pass. It rejects duplicate subjects, colliding
   slugs, mismatched `subject` fields, and two subjects sharing an identical
   topic list.

## Code style

- Python 3.10+, type hints on every public function, `from __future__ import annotations`.
- Docstrings explain *why*, not *what* — the signature already says what.
- Never `except Exception: pass`. Raise a `DailyAILearningError` subclass so the
  CLI can turn it into a real exit code.
- Never `shell=True`. Pass an argument list to `subprocess.run`.
- File writes go through `jsonio.write_json` or `LessonLibrary.write` so a
  crash mid-write cannot corrupt the workspace.
- Nothing outside `paths.py` may hardcode a path. Take a `Paths` instance.

## Commits and pull requests

- One problem per pull request.
- Conventional-ish prefixes are appreciated: `fix:`, `feat:`, `docs:`, `ci:`,
  `refactor:`, `test:`.
- Describe what a reviewer should look at, not what the diff already shows.
- Rebase onto `main` before asking for review.

## Reporting bugs

Open an issue with the output of:

```bash
daily-ai doctor
daily-ai --version
```

Redact anything that looks like a key — although `doctor` only ever prints
whether a key was *found*, never the key itself.

## Code of Conduct

By participating you agree to the [Code of Conduct](CODE_OF_CONDUCT.md).
