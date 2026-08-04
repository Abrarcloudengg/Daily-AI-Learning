[← Docs home](index.md)

# Getting started

## Requirements

- Python 3.10 or newer
- git
- A free [OpenRouter](https://openrouter.ai/keys) API key

## Install

```bash
git clone https://github.com/Abrarcloudengg/Daily-AI-Learning.git
cd Daily-AI-Learning

python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate

python -m pip install -e .
```

`pip install -e .` puts a `daily-ai` command on your `PATH`. If you would rather
not install anything, `python -m daily_ai_learning` and the old
`python scripts/generator.py` both still work.

## Configure

```bash
cp .env.example .env              # Windows: copy .env.example .env
```

Open `.env` and paste your key:

```ini
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

Then confirm everything is wired up:

```bash
daily-ai doctor
```

```
Daily AI Learning doctor

  ✅  Python              3.12.3
  ✅  Workspace           /home/you/Daily-AI-Learning
  ✅  Settings            model=qwen/qwen3-coder, max_tokens=8000
  ✅  OPENROUTER_API_KEY  found
  ✅  Curriculum          15 subjects, 740 topics
  ✅  Git                 branch main
  ✅  Lessons             12 file(s) in generated/
  ✅  Secrets             .env is untracked
  ✅  Environment         local

All checks passed — you are ready to generate.
```

## Generate a lesson

Look before you leap — this costs nothing and calls nothing:

```bash
daily-ai next
daily-ai generate --dry-run
```

Then write it for real:

```bash
daily-ai generate
```

The run writes `generated/<Subject>/Day###_<Topic>.md`, updates
`data/progress.json`, re-renders `README.md`, and commits. Add `--no-git` if you
would rather review the diff yourself first.

## Automate it

The repository ships with `.github/workflows/daily.yml`, which runs at 15:30 UTC
(21:00 IST) every day. To turn it on for your fork:

1. **Settings → Secrets and variables → Actions → New repository secret**
2. Name: `OPENROUTER_API_KEY`, value: your key.
3. **Settings → Actions → General → Workflow permissions →** *Read and write
   permissions*, so the workflow can push its commit.
4. Go to the **Actions** tab, pick **Daily Lesson**, and press **Run workflow**
   to confirm it works before waiting a day.

Local `.env` files do not travel to GitHub. The Actions secret is a separate
thing, and the workflow fails in the first ten seconds with an explicit message
if you forget it.

## Troubleshooting

**`OPENROUTER_API_KEY is not set`** — the key is missing locally (`.env`) or in
CI (repository secret). They are configured independently.

**`402 Payment Required`** — your OpenRouter credit ran out. Switch `model` in
`config/settings.json` to a free-tier slug.

**The lesson was rejected as truncated** — raise `max_tokens`, or lower
`min_lesson_chars` if you genuinely want shorter lessons. Nothing was written and
nothing was marked complete, so simply run it again.

**`git push` was rejected** — someone pushed in between. The pipeline already
rebases and retries; if it still fails, `git pull --rebase` and push manually.

Next: [Configuration](configuration.md) · [CLI reference](cli.md)
