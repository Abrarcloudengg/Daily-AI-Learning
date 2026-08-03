import os
import json
import requests
from dotenv import load_dotenv

from topic_selector import get_next_topic
from git_manager import git_commit_and_push
from readme_updater import update_readme

# ==========================
# Load Environment
# ==========================

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ OPENROUTER_API_KEY not found.")
    exit()

# ==========================
# Get Next Topic
# ==========================

subject, topic = get_next_topic()

if subject is None or topic is None:
    print("✅ All subjects completed.")
    exit()

# ==========================
# Load Progress
# ==========================

with open("data/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

day = progress["day"]
day_number = len(progress["completed"]) + 1

# ==========================
# OpenRouter Request
# ==========================

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/Abrarcloudengg/Daily-AI-Learning",
    "X-Title": "Daily-AI-Learning"
}

payload = {
    "model": "qwen/qwen3-coder",
    "messages": [
        {
            "role": "system",
            "content": (
                "You are a senior programming instructor and technical writer. "
                "Generate detailed, beginner-to-advanced programming lessons in clean Markdown."
            )
        },
        {
            "role": "user",
            "content": f"""
Create a complete professional Markdown lesson.

Subject: {subject}
Day: {day_number}
Topic: {topic}

The lesson must be Beginner → Intermediate → Advanced.

Use EXACTLY this structure.

# {topic}

## Learning Objectives

## Prerequisites

## What is {topic}?

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

Rules:

- Return ONLY Markdown.
- Explain every concept.
- Code must run correctly.
- Use Markdown code blocks.
- Use tables where useful.
- Do not skip sections.
- No placeholder text.
"""
        }
    ],
    "temperature": 0.7,
    "max_tokens": 3500
}

print("🤖 Generating lesson...")

try:

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=payload,
        timeout=120
    )

except Exception as e:
    print("❌ Network Error")
    print(e)
    exit()

if response.status_code != 200:
    print("❌ API Error")
    print(response.status_code)
    print(response.text)
    exit()

result = response.json()

if "choices" not in result:
    print("❌ Invalid Response")
    print(result)
    exit()

lesson = result["choices"][0]["message"]["content"]

# ==========================
# Save Lesson
# ==========================

folder = os.path.join("generated", subject)
os.makedirs(folder, exist_ok=True)

safe_topic = (
    topic.replace(" ", "_")
    .replace("/", "_")
    .replace("\\", "_")
    .replace(":", "")
)

output_file = os.path.join(
    folder,
    f"Day{day_number:03d}_{safe_topic}.md"
)

if os.path.exists(output_file):
    print("⚠ Lesson already exists.")
    print(output_file)
    exit()

with open(output_file, "w", encoding="utf-8") as f:
    f.write(lesson)

# ==========================
# Update Progress
# ==========================

progress["completed"].append(topic)
progress["current_topic"] = topic
progress["day"] += 1

with open("data/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, indent=4)

# ==========================
# Update README
# ==========================

update_readme()

# ==========================
# Success
# ==========================

print()
print("✅ Lesson Generated")
print(f"📚 Subject : {subject}")
print(f"📖 Topic   : {topic}")
print(f"📁 Saved   : {output_file}")

# ==========================
# Git
# ==========================

git_commit_and_push(day_number, topic)