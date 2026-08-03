"""README rendering.

The README is generated, not hand-edited: it doubles as the project's live
dashboard, so every number in it is derived from the catalogue and from the
lessons on disk. Static prose lives in this module next to the dynamic parts so
there is exactly one place to change when the project changes.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

from .catalog import TopicCatalog
from .lessons import LessonLibrary
from .logging_setup import get_logger
from .paths import Paths
from .progress import Progress, ProgressStore
from .settings import Settings

__all__ = ["ReadmeRenderer", "RepoInfo"]

logger = get_logger(__name__)

_PROGRESS_BAR_WIDTH = 24
_GITHUB_URL = re.compile(r"github\.com/(?P<owner>[^/]+)/(?P<repo>[^/#?]+)")


@dataclass(frozen=True)
class RepoInfo:
    """GitHub coordinates used to build badge and link URLs."""

    owner: str = "Abrarcloudengg"
    name: str = "Daily-AI-Learning"

    @classmethod
    def from_settings(cls, settings: Settings) -> RepoInfo:
        """Derive owner/name from the configured referer URL, with fallbacks."""
        match = _GITHUB_URL.search(settings.referer)
        if match is None:
            return cls()
        return cls(owner=match.group("owner"), name=match.group("repo").removesuffix(".git"))

    @property
    def url(self) -> str:
        return f"https://github.com/{self.owner}/{self.name}"

    @property
    def slug(self) -> str:
        return f"{self.owner}/{self.name}"

    @property
    def pages_url(self) -> str:
        return f"https://{self.owner.lower()}.github.io/{self.name}/"


class ReadmeRenderer:
    """Builds ``README.md`` from live project state."""

    def __init__(
        self,
        paths: Paths | None = None,
        catalog: TopicCatalog | None = None,
        store: ProgressStore | None = None,
        settings: Settings | None = None,
        library: LessonLibrary | None = None,
    ) -> None:
        self.paths = paths or Paths.discover()
        self.catalog = catalog or TopicCatalog(self.paths)
        self.library = library or LessonLibrary(self.paths)
        self.store = store or ProgressStore(self.paths, self.catalog, self.library)
        self.settings = settings or Settings()
        self.repo = RepoInfo.from_settings(self.settings)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def write(self, progress: Progress) -> str:
        """Render the README and write it to disk. Returns the content."""
        content = self.render(progress)
        self.paths.readme_file.write_text(content, encoding="utf-8", newline="\n")
        logger.info("Updated %s.", self.paths.relative(self.paths.readme_file))
        return content

    def render(self, progress: Progress) -> str:
        """Return the full README as a Markdown string."""
        sections = (
            self._header(),
            self._about(),
            self._dashboard(progress),
            self._roadmap(progress),
            self._features(),
            self._architecture(),
            self._workflow_diagram(),
            self._structure(),
            self._quickstart(),
            self._configuration(),
            self._usage(),
            self._example_output(),
            self._screenshots(),
            self._automation(),
            self._testing(),
            self._future_plans(),
            self._faq(),
            self._contributing(),
            self._license(),
            self._credits(),
        )
        return "\n\n---\n\n".join(section.strip() for section in sections) + "\n"

    # ------------------------------------------------------------------
    # Sections
    # ------------------------------------------------------------------
    def _header(self) -> str:
        typing_svg = (
            "https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=26"
            "&duration=3200&pause=800&color=58A6FF&center=true&vCenter=true&width=620"
            "&lines=Daily+AI+Learning;One+AI-generated+lesson+every+day;"
            "719+topics.+15+subjects.+Zero+manual+work."
        )
        banner = (
            "https://capsule-render.vercel.app/api?type=waving&color=0:0D1117,50:1F6FEB,100:58A6FF"
            "&height=190&section=header&text=Daily%20AI%20Learning&fontSize=54&fontColor=ffffff"
            "&animation=fadeIn&fontAlignY=36&desc=Your%20curriculum,%20generated%20while%20you%20sleep"
            "&descAlignY=58&descSize=16"
        )

        return f"""<div align="center">

<img src="{banner}" alt="Daily AI Learning" width="100%" />

<a href="{self.repo.url}">
  <img src="{typing_svg}" alt="Daily AI Learning" />
</a>

<p>
  <a href="{self.repo.url}/actions/workflows/daily.yml">
    <img alt="Daily lesson" src="https://img.shields.io/github/actions/workflow/status/{self.repo.slug}/daily.yml?branch=main&label=daily%20lesson&logo=githubactions&logoColor=white&style=for-the-badge" />
  </a>
  <a href="{self.repo.url}/actions/workflows/ci.yml">
    <img alt="CI" src="https://img.shields.io/github/actions/workflow/status/{self.repo.slug}/ci.yml?branch=main&label=ci&logo=github&logoColor=white&style=for-the-badge" />
  </a>
  <a href="{self.repo.url}/blob/main/LICENSE">
    <img alt="License" src="https://img.shields.io/github/license/{self.repo.slug}?style=for-the-badge&color=blue" />
  </a>
  <a href="https://www.python.org/downloads/">
    <img alt="Python" src="https://img.shields.io/badge/python-3.10%2B-3776AB?style=for-the-badge&logo=python&logoColor=white" />
  </a>
</p>

<p>
  <a href="{self.repo.url}/stargazers">
    <img alt="Stars" src="https://img.shields.io/github/stars/{self.repo.slug}?style=flat-square&color=yellow" />
  </a>
  <a href="{self.repo.url}/commits/main">
    <img alt="Last lesson" src="https://img.shields.io/github/last-commit/{self.repo.slug}?style=flat-square&label=last%20lesson" />
  </a>
  <a href="{self.repo.url}/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/{self.repo.slug}?style=flat-square" />
  </a>
  <img alt="Code style" src="https://img.shields.io/badge/code%20style-ruff-261230?style=flat-square&logo=ruff&logoColor=white" />
</p>

<p>
  <a href="#-quickstart"><b>Quickstart</b></a> ·
  <a href="#-configuration"><b>Configuration</b></a> ·
  <a href="#-architecture"><b>Architecture</b></a> ·
  <a href="{self.repo.pages_url}"><b>Docs</b></a> ·
  <a href="#-faq"><b>FAQ</b></a>
</p>

</div>"""

    def _about(self) -> str:
        total = self.catalog.total_topics()
        subjects = len(self.catalog.subjects)

        return f"""## 📖 About

**Daily AI Learning** is a self-driving curriculum. It holds a {total}-topic roadmap across
{subjects} subjects, and every day a GitHub Actions job picks up exactly where it left off,
asks a large language model for the next lesson, validates the result, files it under
`generated/`, refreshes this README, and commits — with nobody at the keyboard.

The interesting part is not the API call. It is everything around it:

| Problem an unattended daily job actually has | How this repo solves it |
|---|---|
| State drifts from reality after a bad merge | `generated/` is the source of truth; progress is **reconciled from disk** every run |
| A crash mid-write corrupts the state file | Every JSON write is **atomic** (temp file + `os.replace`) |
| The model truncates a lesson | Responses are **quality-gated** for truncation, unclosed fences, and missing sections |
| The provider rate-limits or times out | **Exponential backoff with jitter**, honouring `Retry-After` |
| Two runs push at once | Push **rebases and retries** instead of failing |
| Two counters disagree about the day number | There is exactly **one** counter, derived from the lesson files |

The result is a repository that keeps working when you forget it exists."""

    def _dashboard(self, progress: Progress) -> str:
        subjects = self.catalog.subjects
        total_topics = self.catalog.total_topics()
        completed = self.store.global_completed(progress)
        percent = (completed / total_topics * 100) if total_topics else 0.0

        subject_topics = self.catalog.topic_count(progress.subject)
        subject_done = progress.lessons_completed
        subject_percent = (subject_done / subject_topics * 100) if subject_topics else 0.0

        return f"""## 📊 Live Progress

<div align="center">

`{_bar(percent)}`  **{percent:.2f}%**

</div>

| | |
|---|---|
| 📚 **Current subject** | {progress.subject} |
| 🎯 **Current topic** | {progress.current_topic or "—"} |
| 📅 **Next lesson** | Day {progress.day} of {progress.subject} |
| 📈 **Subject progress** | {subject_done}/{subject_topics} · {subject_percent:.1f}% |
| ✅ **Lessons written** | {completed}/{total_topics} |
| 📦 **Subjects finished** | {len(progress.completed_subjects)}/{len(subjects)} |
| 🗂️ **Files on disk** | {self.library.total_count()} Markdown lessons |

> This table is regenerated by `daily-ai readme` on every run. Do not edit it by hand —
> your changes will be overwritten on the next lesson."""

    def _roadmap(self, progress: Progress) -> str:
        rows = []
        for index, subject in enumerate(self.catalog.subjects, start=1):
            topics = self.catalog.topic_count(subject)

            if subject in progress.completed_subjects:
                status, done = "✅ Done", topics
            elif subject == progress.subject:
                status, done = "🚀 In progress", progress.lessons_completed
            else:
                status, done = "📘 Queued", self.library.count(subject)

            percent = (done / topics * 100) if topics else 0.0
            folder = self.catalog.lesson_folder(subject)
            link = f"[`{folder}/`](generated/{folder})"
            rows.append(
                f"| {index} | **{subject}** | {status} | {done}/{topics} | `{_bar(percent, 12)}` | {link} |"
            )

        table = "\n".join(rows)
        flow = " → ".join(self.catalog.subjects)

        return f"""## 🗺️ Roadmap

| # | Subject | Status | Lessons | Progress | Folder |
|---:|---|---|---:|---|---|
{table}

**Learning flow**

```text
{flow}
```"""

    def _features(self) -> str:
        return """## ✨ Features

**Content**

- 🧠 Beginner → Intermediate → Advanced in a single lesson
- 📐 24 fixed sections per lesson: theory, syntax, three worked examples, output, pitfalls, best practices
- 🎯 10 interview questions, 10 MCQs, 10 practice questions, 5 coding exercises
- 🛠️ A mini project and an assignment in every lesson

**Engineering**

- ♻️ Idempotent — a topic is never generated twice, even if state is lost
- 🔁 Self-healing — progress is rebuilt from the filesystem on every run
- 🛡️ Atomic writes — an interrupted run cannot corrupt state
- 🌐 Resilient networking — retries with jitter, `Retry-After` aware, typed errors
- 🔍 Quality gates — truncated or malformed lessons are rejected, not committed
- 🧪 Tested — pytest suite covering naming, progress, selection, and rendering
- 📋 Real logging — levels, timestamps in CI, UTF-8 safe on Windows
- 🧩 Typed — full type hints, `ruff` + `mypy` clean in CI
- 🖥️ Cross-platform — identical behaviour on Windows, macOS, and Linux"""

    def _architecture(self) -> str:
        return """## 🏗️ Architecture

Every module has one job and no module reaches around another.

```mermaid
flowchart TB
    subgraph CFG["⚙️ Configuration"]
        S["settings.py<br/><i>model, retries, limits</i>"]
        P["paths.py<br/><i>one source of truth<br/>for the filesystem</i>"]
        N["naming.py<br/><i>subject → slug → folder</i>"]
    end

    subgraph DOM["📚 Domain"]
        C["catalog.py<br/><i>subjects + topics</i>"]
        L["lessons.py<br/><i>the library on disk</i>"]
        PR["progress.py<br/><i>state + reconciliation</i>"]
        SEL["selector.py<br/><i>what comes next</i>"]
    end

    subgraph IO["🌐 Adapters"]
        PROV["provider.py<br/><i>OpenRouter + retries</i>"]
        PRM["prompts.py<br/><i>template + quality gates</i>"]
        RM["readme.py<br/><i>dashboard renderer</i>"]
        GIT["git_ops.py<br/><i>commit &amp; push</i>"]
    end

    CLI["cli.py"] --> PIPE["pipeline.py<br/><b>orchestration</b>"]
    PIPE --> SEL --> C & L & PR
    PIPE --> PROV --> PRM
    PIPE --> L
    PIPE --> RM
    PIPE --> GIT
    CFG -.-> DOM
    CFG -.-> IO

    classDef cfg fill:#1F6FEB22,stroke:#1F6FEB,stroke-width:1px
    classDef dom fill:#3FB95022,stroke:#3FB950,stroke-width:1px
    classDef io  fill:#DB6D2822,stroke:#DB6D28,stroke-width:1px
    class S,P,N cfg
    class C,L,PR,SEL dom
    class PROV,PRM,RM,GIT io
```

**Design rules**

1. **The filesystem is the database.** `data/progress.json` is a cache and is always
   rebuilt from `generated/` before any decision is made.
2. **Paths are injected, never assumed.** Nothing resolves a path from the current
   working directory, so the tests run against a `tmp_path` workspace.
3. **Failures are typed.** Every deliberate error subclasses `DailyAILearningError`
   and carries a process exit code.
4. **The pipeline decides, the modules execute.** Only `pipeline.py` knows the order
   of operations."""

    def _workflow_diagram(self) -> str:
        return """## 🔄 How a Run Works

```mermaid
sequenceDiagram
    autonumber
    participant CRON as ⏰ GitHub Actions
    participant CLI as 🖥️ daily-ai generate
    participant DISK as 📁 generated/
    participant SEL as 🎯 Selector
    participant AI as 🤖 OpenRouter
    participant GIT as 🔀 Git

    CRON->>CLI: scheduled run (15:30 UTC)
    CLI->>DISK: list existing lessons
    DISK-->>SEL: what is already taught
    SEL->>SEL: reconcile progress with disk
    SEL-->>CLI: next subject + topic + day

    CLI->>AI: chat completion (system + lesson template)
    alt transient failure
        AI-->>CLI: 429 / 5xx / timeout
        CLI->>AI: retry with exponential backoff + jitter
    end
    AI-->>CLI: Markdown lesson

    CLI->>CLI: quality gate (truncation, fences, sections)
    alt lesson rejected
        CLI-->>CRON: exit non-zero, nothing written
    else lesson accepted
        CLI->>DISK: write DayNNN_Topic.md (atomic)
        CLI->>DISK: update progress.json (atomic)
        CLI->>DISK: regenerate README.md
        CLI->>GIT: pull --rebase, commit, push
        GIT-->>CRON: ✅ Day N: Topic
    end
```"""

    def _structure(self) -> str:
        folders = [self.catalog.lesson_folder(subject) for subject in self.catalog.subjects]
        preview = "\n".join(f"│   ├── {folder}/" for folder in folders[:4])
        remaining = len(folders) - 4

        return f"""## 📂 Project Structure

```text
Daily-AI-Learning/
├── .github/
│   ├── ISSUE_TEMPLATE/          # Bug report + feature request forms
│   └── workflows/
│       ├── daily.yml            # ⏰ The scheduled lesson generator
│       ├── ci.yml               # ✅ Lint, type-check, test on every push
│       ├── pages.yml            # 📄 Publishes docs/ to GitHub Pages
│       └── release.yml          # 🏷️ Tag → GitHub Release
├── config/
│   ├── settings.json            # Model, token budget, retry policy
│   ├── subjects.json            # The roadmap, in teaching order
│   └── topics/                  # One <subject>_topics.json per subject
├── data/
│   └── progress.json            # Generated state (rebuilt from disk if lost)
├── docs/                        # GitHub Pages site
├── generated/                   # 📚 The lessons
{preview}
│   └── … {remaining} more subjects
├── src/daily_ai_learning/       # 🧠 The package
│   ├── catalog.py               # Subjects and topics
│   ├── cli.py                   # Command line interface
│   ├── git_ops.py               # Commit and push
│   ├── lessons.py               # The lesson library on disk
│   ├── naming.py                # Subject → slug → folder mapping
│   ├── paths.py                 # Workspace layout
│   ├── pipeline.py              # Orchestration
│   ├── progress.py              # State + reconciliation
│   ├── prompts.py               # Lesson template + quality gates
│   ├── provider.py              # OpenRouter client
│   ├── readme.py                # This file's generator
│   ├── selector.py              # What to teach next
│   └── settings.py              # Configuration
├── scripts/                     # Thin shims: legacy `python scripts/generator.py`
└── tests/                       # pytest suite
```"""

    def _quickstart(self) -> str:
        return f"""## 🚀 Quickstart

> **Requirements** — Python 3.10+, git, and a free [OpenRouter](https://openrouter.ai/keys) API key.

```bash
# 1. Clone
git clone {self.repo.url}.git
cd {self.repo.name}

# 2. Create an isolated environment
python -m venv venv
source venv/bin/activate          # Windows: venv\\Scripts\\activate

# 3. Install
pip install -e .                  # add "[dev]" for the test and lint tools

# 4. Add your API key
cp .env.example .env              # Windows: copy .env.example .env
#    then edit .env and paste your OpenRouter key

# 5. Check the setup before spending a token
daily-ai doctor

# 6. Generate today's lesson
daily-ai generate
```

**No installation?** The legacy entry point still works:

```bash
pip install -r requirements.txt
python scripts/generator.py
```

### Run it on autopilot

1. Fork or push this repository to GitHub.
2. Go to **Settings → Secrets and variables → Actions → New repository secret**.
3. Name it `OPENROUTER_API_KEY` and paste your key.
4. Open the **Actions** tab and enable workflows.

That is the whole setup. A lesson lands every day at **15:30 UTC (21:00 IST)**, and
you can trigger one immediately from **Actions → Daily Lesson → Run workflow**."""

    def _configuration(self) -> str:
        defaults = Settings()

        return f"""## ⚙️ Configuration

Three layers, each overriding the one above it.

**1. `config/settings.json`** — the reviewable defaults:

| Key | Default | What it controls |
|---|---|---|
| `model` | `{defaults.model}` | Any [OpenRouter model](https://openrouter.ai/models) slug |
| `max_tokens` | `{defaults.max_tokens}` | Response budget. Below ~6000 the template gets truncated |
| `temperature` | `{defaults.temperature}` | Creativity. Lower is more consistent |
| `max_retries` | `{defaults.max_retries}` | Attempts before the run gives up |
| `retry_backoff` | `{defaults.retry_backoff}` | Seconds for the first retry; doubles each time |
| `request_timeout` | `{defaults.request_timeout}` | Seconds to wait for one response |
| `min_lesson_chars` | `{defaults.min_lesson_chars}` | Shorter responses are treated as truncated |
| `lessons_per_run` | `{defaults.lessons_per_run}` | Lessons generated per invocation |
| `log_level` | `{defaults.log_level}` | `DEBUG`, `INFO`, `WARNING`, `ERROR` |
| `git_remote` / `git_branch` | `{defaults.git_remote}` / `{defaults.git_branch}` | Push target |

**2. Environment variables** — `DAILY_AI_<KEY>` overrides any of the above for one run:

```bash
DAILY_AI_MODEL=anthropic/claude-sonnet-4 DAILY_AI_LOG_LEVEL=DEBUG daily-ai generate
```

**3. Secrets** — never in a file that git tracks:

| Variable | Where it goes |
|---|---|
| `OPENROUTER_API_KEY` | `.env` locally, an Actions secret in CI |

### Customising the curriculum

Add a subject in three steps:

```jsonc
// 1. config/subjects.json — append it in teaching order
{{ "subjects": ["Python", "Git", "Rust"] }}
```

```jsonc
// 2. config/topics/rust_topics.json — the file name is the lower-cased,
//    non-alphanumeric-stripped subject name
{{ "subject": "Rust", "topics": ["Ownership", "Borrowing", "Lifetimes"] }}
```

```bash
# 3. Verify before the scheduler finds the mistake for you
daily-ai validate
```"""

    def _usage(self) -> str:
        return """## 🖥️ Usage

```bash
daily-ai generate              # write the next lesson (default: 1)
daily-ai generate --count 5    # catch up on five lessons in one go
daily-ai generate --dry-run    # show what would happen; no API call, no writes
daily-ai generate --no-git     # generate and save, but do not commit or push

daily-ai next                  # which topic is next?
daily-ai status                # full progress dashboard in the terminal
daily-ai readme                # regenerate README.md only (free, no API call)
daily-ai validate              # check every config file for problems
daily-ai doctor                # verify environment, key, git, and config
daily-ai version               # print the version
```

Every command accepts `--log-level DEBUG` for a full trace, and `--root PATH` to run
against a checkout other than the current one.

**Exit codes** are meaningful, so CI can branch on them:

| Code | Meaning |
|---:|---|
| `0` | Success, or nothing left to do |
| `65` | Bad data — a malformed topic file or progress file |
| `69` | The model provider failed after every retry |
| `70` | A lesson was generated but failed the quality gate |
| `78` | Bad configuration — usually a missing API key |
| `130` | Interrupted with Ctrl-C |"""

    def _example_output(self) -> str:
        return """## 📤 Example Output

```console
$ daily-ai generate
📚 Python · Day 9 · While Loop  (9/114)
Requesting lesson from qwen/qwen3-coder (attempt 1/3)…
Received 21418 characters (finish_reason=stop, tokens=7734).
✅ Quality gate passed: 24/24 sections, 21418 characters.
📝 Wrote generated/Python/Day009_While_Loop.md
📊 Updated README.md
🔀 Committed: Day 9: While Loop (Python)
🚀 Pushed to origin/main

Done in 48.2s.
```

Each generated lesson follows the same 24-section shape:

```markdown
# While Loop

## Learning Objectives
## Prerequisites
## What is While Loop?
## Why is it Important?
## Real World Analogy
## Theory
## Syntax
## Flow / Working
## Example 1 (Beginner)
## Example 2 (Intermediate)
## Example 3 (Advanced)
## Output
## Common Mistakes
## Best Practices
## Pro Tips
## Interview Questions (10)
## MCQs (10)
## Practice Questions (10)
## Coding Exercises (5)
## Mini Project
## Assignment
## Summary
## Key Takeaways
## Next Topic Preview
```

📖 **Read a real one:** [`generated/Python/Day001_Variables.md`](generated/Python/Day001_Variables.md)"""

    def _screenshots(self) -> str:
        return """## 📸 Screenshots

<div align="center">

<!-- Replace these placeholders with real captures: docs/assets/*.png -->

| Terminal run | GitHub Actions |
|---|---|
| <img src="docs/assets/screenshot-cli.png" alt="CLI run" width="420" /> | <img src="docs/assets/screenshot-actions.png" alt="Actions run" width="420" /> |

| A generated lesson | Progress dashboard |
|---|---|
| <img src="docs/assets/screenshot-lesson.png" alt="Generated lesson" width="420" /> | <img src="docs/assets/screenshot-readme.png" alt="README dashboard" width="420" /> |

</div>"""

    def _automation(self) -> str:
        return f"""## 🤖 Automation

| Workflow | Trigger | What it does |
|---|---|---|
| [`daily.yml`]({self.repo.url}/blob/main/.github/workflows/daily.yml) | `schedule` 15:30 UTC · manual | Generates the next lesson and commits it |
| [`ci.yml`]({self.repo.url}/blob/main/.github/workflows/ci.yml) | push · pull request | `ruff`, `mypy`, and `pytest` on Linux, macOS, and Windows |
| [`pages.yml`]({self.repo.url}/blob/main/.github/workflows/pages.yml) | push to `main` | Publishes `docs/` to GitHub Pages |
| [`release.yml`]({self.repo.url}/blob/main/.github/workflows/release.yml) | tag `v*` | Builds the package and drafts a GitHub Release |

The daily job runs with `concurrency` enabled, so a manual run and a scheduled run can
never race each other into a merge conflict.

**Manual trigger with options:**

Actions → *Daily Lesson* → *Run workflow* → set `count` (how many lessons) or `dry_run`."""

    def _testing(self) -> str:
        return """## 🧪 Development

```bash
pip install -e ".[dev]"

pytest                       # run the suite
pytest --cov=daily_ai_learning --cov-report=term-missing

ruff check .                 # lint
ruff format .                # format
mypy src                     # type-check
```

The tests never touch the network and never touch your real workspace: `tests/conftest.py`
builds a throwaway repository under `tmp_path` and points `DAILY_AI_ROOT` at it."""

    def _future_plans(self) -> str:
        return """## 🔭 Roadmap

Ideas that fit the existing architecture, roughly in order of value:

| | Feature | Sketch |
|---|---|---|
| 🧠 | **Spaced repetition** | Schedule revision lessons at 1/3/7/21 days using the day numbers already on disk |
| ❓ | **Quiz generator** | Extract the MCQ section of each lesson into a runnable `quiz` command |
| 🃏 | **Flashcards** | Emit Anki-compatible CSV from *Key Takeaways* |
| 📄 | **PDF export** | Bundle a finished subject into a single typeset PDF |
| 🎓 | **Certificates** | Generate a completion certificate when a subject reaches 100% |
| 📊 | **Analytics** | Streaks, velocity, and time-to-completion charts in the README |
| 🗓️ | **Weekly digest** | Summarise the week's lessons into one recap file |
| 🧩 | **Project generator** | Chain finished topics into an end-of-subject capstone project |
| 🏆 | **Achievements** | Badges for streaks and subject completions |
| 🌍 | **Multi-language** | Generate the same curriculum in another spoken language |
| 🔀 | **Model fallback** | Automatically fall back to a second model when the first is unavailable |
| 🔊 | **Audio lessons** | Text-to-speech version of each lesson for commutes |

Want one of these? [Open an issue](../../issues/new/choose) — or build it and open a PR."""

    def _faq(self) -> str:
        return """## ❓ FAQ

<details>
<summary><b>Does it cost anything to run?</b></summary>

OpenRouter has free-tier models, and the default `qwen/qwen3-coder` is inexpensive.
One lesson is a single request of roughly 8k output tokens. GitHub Actions minutes are
free on public repositories.
</details>

<details>
<summary><b>What happens if a run fails halfway through?</b></summary>

Nothing breaks. A lesson is written only after it passes the quality gate, and every
state write is atomic. On the next run, progress is rebuilt from the files that exist,
so the failed topic is simply attempted again.
</details>

<details>
<summary><b>Can I use a different model?</b></summary>

Yes. Change `model` in `config/settings.json` to any
[OpenRouter model slug](https://openrouter.ai/models), or set `DAILY_AI_MODEL` for a
single run. Nothing else in the codebase is provider-specific.
</details>

<details>
<summary><b>Why is `data/progress.json` committed if it is generated?</b></summary>

So the README dashboard is correct on GitHub without running anything. It is treated as
a cache: if it is lost, corrupted, or mangled by a merge, the next run rebuilds it from
`generated/`. That is what `progress.reconcile()` exists for.
</details>

<details>
<summary><b>Will it ever generate the same lesson twice?</b></summary>

No. Selection asks the filesystem, not the state file. A topic with a
`DayNNN_Topic.md` file is skipped even if `progress.json` has never heard of it.
</details>

<details>
<summary><b>How do I catch up after missing a few days?</b></summary>

`daily-ai generate --count 7`. Lessons are numbered by position, not by calendar date,
so nothing gets out of order.
</details>

<details>
<summary><b>The emoji look like <code>ðŸš€</code> in my terminal. Is the file corrupt?</b></summary>

No — that is PowerShell's legacy console encoding, not the file. Use
`Get-Content README.md -Encoding UTF8`, or run `chcp 65001` once per session. The file
itself is valid UTF-8.
</details>

<details>
<summary><b>Can I add my own subject?</b></summary>

Yes, and it takes two files: append the subject to `config/subjects.json` and add
`config/topics/<slug>_topics.json`. Run `daily-ai validate` to confirm the wiring.
</details>"""

    def _contributing(self) -> str:
        return f"""## 🤝 Contributing

Contributions are welcome — new subjects, better prompts, bug fixes, docs.

1. Read [CONTRIBUTING.md]({self.repo.url}/blob/main/CONTRIBUTING.md)
2. Fork, branch, and make your change
3. Run `pytest` and `ruff check .`
4. Open a pull request using the template

Please also read the [Code of Conduct]({self.repo.url}/blob/main/CODE_OF_CONDUCT.md)
and, for anything security-related, [SECURITY.md]({self.repo.url}/blob/main/SECURITY.md)."""

    def _license(self) -> str:
        return f"""## 📜 License

Released under the [MIT License]({self.repo.url}/blob/main/LICENSE).

The generated lessons are produced by a language model. They are a study aid, not a
substitute for official documentation — verify anything you intend to rely on."""

    def _credits(self) -> str:
        return f"""## 💙 Credits

Built by **[Abrar Patel](https://github.com/{self.repo.owner})**.

Standing on: [OpenRouter](https://openrouter.ai) · [GitHub Actions](https://github.com/features/actions) ·
[Requests](https://requests.readthedocs.io) · [Ruff](https://docs.astral.sh/ruff/) ·
[pytest](https://docs.pytest.org) · [Shields.io](https://shields.io) ·
[Mermaid](https://mermaid.js.org)

<div align="center">

**If this project is useful to you, a ⭐ helps others find it.**

<a href="{self.repo.url}/stargazers">
  <img src="https://img.shields.io/github/stars/{self.repo.slug}?style=social" alt="Star this repository" />
</a>

<sub>Every lesson in this repository was written by a machine that never misses a day.</sub>

</div>"""


def _bar(percent: float, width: int = _PROGRESS_BAR_WIDTH) -> str:
    """Render a text progress bar, e.g. ``███░░░░░░░``."""
    clamped = max(0.0, min(100.0, percent))
    filled = round(width * clamped / 100)
    return "█" * filled + "░" * (width - filled)
