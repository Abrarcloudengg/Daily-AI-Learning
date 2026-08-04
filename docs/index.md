# Daily AI Learning

An autonomous curriculum generator. Every day at 21:00 IST a GitHub Actions
workflow picks the next unwritten topic from a 740-topic roadmap, asks an LLM to
write a full lesson on it, saves the lesson as Markdown, updates the progress
dashboard in the README, and pushes the commit. Nobody presses a button.

## Documentation

| Page | What it covers |
| --- | --- |
| [Getting started](getting-started.md) | Install, configure, and generate your first lesson |
| [Configuration](configuration.md) | Every key in `config/settings.json` and its environment override |
| [CLI reference](cli.md) | All seven commands, their flags, and their exit codes |
| [Architecture](architecture.md) | How the modules fit together and why they are split that way |
| [Automation](automation.md) | The four GitHub Actions workflows |
| [Curriculum](curriculum.md) | Adding subjects and topics |
| [FAQ](faq.md) | The questions people actually ask |

## The 30-second version

```bash
python -m pip install -e .
echo "OPENROUTER_API_KEY=sk-or-v1-..." > .env
daily-ai doctor      # confirm the environment is sane
daily-ai next        # what would be generated next
daily-ai generate    # write it
```

## Design principles

**The filesystem is the source of truth.** `data/progress.json` is a cache. On
every run the completed list is rebuilt from what is actually present in
`generated/`, so a merge conflict, a manual deletion, or a killed job repairs
itself instead of desynchronising forever.

**Never mark work done that was not done.** The lesson file is written before
progress is updated, and a lesson that came back truncated or too short is
rejected rather than saved. A crash costs you one API call, never a permanently
skipped topic.

**Every write is atomic.** Temporary file, `fsync`, `os.replace`. A cancelled
Actions run cannot leave half a JSON document on disk.

**Configuration is not code.** Model, temperature, token budget, retry policy,
and quality thresholds live in `config/settings.json`, and any of them can be
overridden for a single run with a `DAILY_AI_*` environment variable.

**Failures have exit codes.** Bad data is 65, provider trouble is 69, a failed
generation is 70, a misconfiguration is 78. CI can tell them apart.

---

[View on GitHub](https://github.com/Abrarcloudengg/Daily-AI-Learning) ·
[MIT licensed](https://github.com/Abrarcloudengg/Daily-AI-Learning/blob/main/LICENSE)
