import os

from common import (
    FOLDER_OVERRIDES,
    README_FILE,
    load_json,
    load_progress,
    load_subjects,
    topic_file,
)


def count_topics(subject):
    path = topic_file(subject)

    if not os.path.exists(path):
        return 0

    return len(load_json(path)["topics"])


def get_total_topics(subjects):
    return sum(count_topics(subject) for subject in subjects)


def get_completed_topics(progress):

    completed = len(progress.get("completed", []))

    for subject in progress.get("completed_subjects", []):
        completed += count_topics(subject)

    return completed


def build_roadmap(subjects, progress):

    lines = []

    for subject in subjects:

        if subject in progress.get("completed_subjects", []):
            icon = "✅"

        elif subject == progress.get("subject"):
            icon = "🚀"

        else:
            icon = "📘"

        lines.append(f"- {icon} {subject} ({count_topics(subject)} topics)")

    return "\n".join(lines)


def build_lesson_tree(subjects):

    folders = [FOLDER_OVERRIDES.get(s, s) for s in subjects]

    lines = ["generated/"]

    for folder in folders[:-1]:
        lines.append(f"├── {folder}/")

    lines.append(f"└── {folders[-1]}/")

    return "\n".join(lines)


def update_readme():

    progress = load_progress()
    subjects = load_subjects()

    total_topics = get_total_topics(subjects)
    completed_topics = get_completed_topics(progress)

    percentage = round((completed_topics / total_topics) * 100, 2) if total_topics else 0

    readme = f"""# 🚀 Daily AI Learning

Automatically generated programming lessons using AI.

---

# 📊 Progress

| Item | Value |
|------|------|
| 📚 Current Subject | {progress.get("subject", "-")} |
| 📖 Current Day | {progress.get("day", 1)} |
| 🎯 Current Topic | {progress.get("current_topic") or "-"} |
| ✅ Completed Topics | {completed_topics}/{total_topics} |
| 📦 Completed Subjects | {len(progress.get("completed_subjects", []))}/{len(subjects)} |
| 📈 Progress | {percentage}% |

---

# 📚 Learning Roadmap

{build_roadmap(subjects, progress)}

---

# 🤖 Features

- ✅ Automatic Topic Selection
- ✅ Automatic Subject Switching
- ✅ AI Lesson Generation
- ✅ README Auto Update
- ✅ Git Auto Commit
- ✅ Git Auto Push
- ✅ GitHub Actions
- ✅ Beginner → Advanced
- ✅ Mini Projects
- ✅ Coding Exercises

---

# 📂 Folder Structure

```text
Daily-AI-Learning/
├── .github/workflows/   # Daily scheduled run
├── config/              # Subject list + topic lists
├── data/                # progress.json (generated state)
├── generated/           # Lessons, one folder per subject
├── scripts/             # Generator, topic selector, README + git helpers
└── requirements.txt
```

---

# 📁 Generated Lessons

Lessons are automatically generated inside:

```text
{build_lesson_tree(subjects)}
```

---

# 📖 Learning Flow

{" → ".join(subjects)}

---

# 🚀 Tech Stack

- Python
- OpenRouter API
- GitHub Actions
- Markdown
- JSON

---

Made with ❤️ by Abrar Patel
"""

    with open(README_FILE, "w", encoding="utf-8") as f:
        f.write(readme)

    print("✅ README Updated Successfully!")


if __name__ == "__main__":
    update_readme()
