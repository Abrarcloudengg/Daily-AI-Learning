import json

def update_readme():

    with open("data/progress.json", "r", encoding="utf-8") as f:
        progress = json.load(f)

    subject = progress["subject"]
    day = progress["day"]
    topic = progress["current_topic"]
    completed = len(progress["completed"])

    readme = f"""# 🚀 Daily AI Learning

Automatically generated programming lessons using AI.

---

## 📊 Progress

| Item | Value |
|------|-------|
| 📚 Subject | {subject} |
| 📅 Current Day | {day} |
| 📝 Latest Topic | {topic} |
| ✅ Lessons Completed | {completed} |

---

## 📂 Subjects

- Python
- SQL
- Git
- Linux
- JavaScript
- React
- NodeJS
- Docker
- AWS
- DSA

---

🤖 Generated Automatically using OpenRouter + GitHub Actions.
"""

    with open("README.md", "w", encoding="utf-8") as f:
        f.write(readme)