import os
import sys
import time

import requests
from dotenv import load_dotenv

from common import (
    lesson_dir,
    load_progress,
    safe_topic_name,
    save_progress,
)
from git_manager import git_commit_and_push
from readme_updater import update_readme
from topic_selector import get_next_topic

MODEL = "qwen/qwen3-coder"
MAX_TOKENS = 8000
MAX_RETRIES = 3

# ==========================
# Load Environment
# ==========================

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ OPENROUTER_API_KEY not found.")
    sys.exit(1)

# ==========================
# Get Next Topic
# ==========================

subject, topic = get_next_topic()

if subject is None or topic is None:
    print("✅ All subjects completed.")
    sys.exit(0)

progress = load_progress()

day_number = len(progress["completed"]) + 1

print(f"📚 Subject : {subject}")
print(f"📖 Topic   : {topic}")
print(f"📅 Day     : {day_number}")

# ==========================
# OpenRouter Request
# ==========================

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/Abrarcloudengg/Daily-AI-Learning",
    "X-Title": "Daily-AI-Learning",
}

payload = {
    "model": MODEL,
    "messages": [
        {
            "role": "system",
            "content": (
                "You are a senior programming instructor and technical writer. "
                "Generate detailed, beginner-to-advanced programming lessons in clean Markdown."
            ),
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
- Finish every section. Never stop mid-sentence.
""",
        },
    ],
    "temperature": 0.7,
    "max_tokens": MAX_TOKENS,
}


def request_lesson():
    """Call OpenRouter, retrying transient failures. Returns (markdown, finish_reason)."""

    for attempt in range(1, MAX_RETRIES + 1):

        print(f"🤖 Generating lesson... (attempt {attempt}/{MAX_RETRIES})")

        try:
            response = requests.post(
                "https://openrouter.ai/api/v1/chat/completions",
                headers=headers,
                json=payload,
                timeout=180,
            )
        except requests.RequestException as e:
            print(f"⚠ Network error: {e}")
            time.sleep(5 * attempt)
            continue

        if response.status_code in (429, 500, 502, 503, 504):
            print(f"⚠ API returned {response.status_code}, retrying...")
            time.sleep(5 * attempt)
            continue

        if response.status_code != 200:
            print("❌ API Error")
            print(response.status_code)
            print(response.text)
            return None, None

        try:
            result = response.json()
        except ValueError:
            print("⚠ Response was not JSON, retrying...")
            time.sleep(5 * attempt)
            continue

        if not result.get("choices"):
            print("⚠ Invalid response, retrying...")
            print(result)
            time.sleep(5 * attempt)
            continue

        choice = result["choices"][0]

        return choice["message"]["content"], choice.get("finish_reason")

    print("❌ Giving up after repeated failures.")
    return None, None


lesson, finish_reason = request_lesson()

if not lesson or not lesson.strip():
    sys.exit(1)

if finish_reason == "length":
    print("⚠ Lesson hit the token limit and may be cut short.")

# ==========================
# Save Lesson
# ==========================

folder = lesson_dir(subject)
os.makedirs(folder, exist_ok=True)

output_file = os.path.join(
    folder,
    f"Day{day_number:03d}_{safe_topic_name(topic)}.md",
)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(lesson)

# ==========================
# Update Progress
# ==========================

progress["completed"].append(topic)
progress["current_topic"] = topic
progress["day"] = len(progress["completed"]) + 1

save_progress(progress)

# ==========================
# Update README
# ==========================

update_readme()

print()
print("✅ Lesson Generated")
print(f"📁 Saved   : {output_file}")

# ==========================
# Git
# ==========================

# In CI the workflow owns the commit step; committing here too would
# double-commit and fail anyway (git identity is configured later).
if os.getenv("GITHUB_ACTIONS") == "true":
    print("ℹ Running in GitHub Actions — workflow will handle the commit.")
else:
    git_commit_and_push(day_number, topic)
