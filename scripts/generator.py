import os
import json
import requests
from readme_updater import update_readme
from dotenv import load_dotenv
from topic_selector import get_next_topic
from git_manager import git_commit_and_push

# Load .env
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

if not API_KEY:
    print("❌ OPENROUTER_API_KEY not found.")
    exit()

# Get next topic automatically
subject, topic = get_next_topic()

if topic is None:
    print("✅ All topics completed.")
    exit()

# Read current progress
with open("data/progress.json", "r", encoding="utf-8") as f:
    progress = json.load(f)

day = progress["day"]

headers = {
    "Authorization": f"Bearer {API_KEY}",
    "Content-Type": "application/json",
    "HTTP-Referer": "https://github.com/Abrarcloudengg/Daily-AI-Learning",
    "X-Title": "Daily-AI-Learning"
}

data = {
    "model": "qwen/qwen3-coder",
    "messages": [
        {
            "role": "system",
            "content": (
                "You are a senior programming instructor and technical writer. "
                "Generate professional, detailed, beginner-to-advanced programming lessons in Markdown."
            )
        },
        {
            "role": "user",
            "content": f"""
Create a complete professional Markdown lesson.

Subject: {subject}
Day: {day}
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
- Use proper Markdown headings.
- Explain every concept clearly.
- Every code example must run correctly.
- Use Python markdown code blocks.
- Use tables wherever useful.
- Make the lesson interview-ready.
- Do NOT skip any section.
- Do NOT use placeholder text.
- Keep explanations detailed and professional.
"""
        }
    ],
    "max_tokens": 3500,
    "temperature": 0.7
}

response = requests.post(
    "https://openrouter.ai/api/v1/chat/completions",
    headers=headers,
    json=data,
)

if response.status_code != 200:
    print("❌ Error:", response.status_code)
    print(response.text)
    exit()

lesson = response.json()["choices"][0]["message"]["content"]

# Create subject folder
os.makedirs(f"generated/{subject}", exist_ok=True)

# Safe filename
safe_topic = topic.replace(" ", "_").replace("/", "_")

output_file = (
    f"generated/{subject}/"
    f"Day{day:03d}_{safe_topic}.md"
)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(lesson)

update_readme()

print("✅ Lesson generated successfully!")
print(f"📚 Subject : {subject}")
print(f"📚 Topic   : {topic}")
print(f"📁 Saved   : {output_file}")

# Commit & Push
git_commit_and_push(day, topic)