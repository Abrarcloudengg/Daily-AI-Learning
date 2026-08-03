import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROGRESS_FILE = os.path.join(BASE_DIR, "data", "progress.json")
SUBJECTS_FILE = os.path.join(BASE_DIR, "config", "subjects.json")
README_FILE = os.path.join(BASE_DIR, "README.md")


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def get_total_topics():
    total = 0

    subjects = load_json(SUBJECTS_FILE)["subjects"]

    for subject in subjects:

        topic_file = os.path.join(
            BASE_DIR,
            "config",
            f"{subject.lower()}_topics.json"
        )

        if os.path.exists(topic_file):
            total += len(load_json(topic_file)["topics"])

    return total


def get_completed_topics(progress):

    completed = len(progress.get("completed", []))

    for subject in progress.get("completed_subjects", []):

        topic_file = os.path.join(
            BASE_DIR,
            "config",
            f"{subject.lower()}_topics.json"
        )

        if os.path.exists(topic_file):
            completed += len(load_json(topic_file)["topics"])

    return completed


def update_readme():

    progress = load_json(PROGRESS_FILE)

    subjects = load_json(SUBJECTS_FILE)["subjects"]

    total_topics = get_total_topics()

    completed_topics = get_completed_topics(progress)

    percentage = round(
        (completed_topics / total_topics) * 100,
        2
    ) if total_topics else 0

    roadmap = ""

    for subject in subjects:

        if subject in progress.get("completed_subjects", []):
            icon = "✅"

        elif subject == progress.get("subject"):
            icon = "🚀"

        else:
            icon = "📘"

        roadmap += f"- {icon} {subject}\n"

    readme = f"""# 🚀 Daily AI Learning

Automatically generated programming lessons using AI.

---

# 📊 Progress

| Item | Value |
|------|------|
| 📚 Current Subject | {progress["subject"]} |
| 📖 Current Day | {progress["day"]} |
| 🎯 Current Topic | {progress["current_topic"]} |
| ✅ Completed Topics | {completed_topics}/{total_topics} |
| 📦 Completed Subjects | {len(progress["completed_subjects"])}/{len(subjects)} |
| 📈 Progress | {percentage}% |

---

# 📚 Learning Roadmap

{roadmap}

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
---

# 📁 Generated Lessons

Lessons are automatically generated inside:

```text
generated/
├── Python/
├── Git/
├── SQL/
├── Linux/
├── AWS/
├── Docker/
├── Kubernetes/
├── HTML/
├── CSS/
├── JavaScript/
├── React/
├── NodeJS/
├── DSA/
├── AI/
└── LangChain/
```

---

# 📖 Learning Flow

Python → Git → SQL → Linux → AWS → Docker → Kubernetes → HTML → CSS → JavaScript → React → NodeJS → DSA → AI → LangChain

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
