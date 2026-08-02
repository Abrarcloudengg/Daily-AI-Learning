import os
import json
import requests
from dotenv import load_dotenv
from topic_selector import get_next_topic
from git_manager import git_commit_and_push

# Load .env
load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")

# Get next topic automatically
topic = get_next_topic()

# Read current day
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
            "content": "You are an expert programming teacher. Create high-quality Markdown lessons."
        },
        {
            "role": "user",
            "content": f"""
Create Day {day} of Python Learning.

Topic: {topic}

Include:

# Title

## Explanation

## Syntax

## Example Code

## Output

## Common Mistakes

## Interview Questions

## Practice Questions

## Assignment

Return ONLY Markdown.
"""
        }
    ],
    "max_tokens": 1800,
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

# Create folder if not exists
os.makedirs("generated/Python", exist_ok=True)

# Safe filename
safe_topic = topic.replace(" ", "_")

output_file = f"generated/Python/Day{day:03d}_{safe_topic}.md"

with open(output_file, "w", encoding="utf-8") as f:
    f.write(lesson)

# Update progress
# Update progress

completed = progress["completed"]
day = progress["day"]

completed.append(topic)
day += 1

progress["completed"] = completed
progress["day"] = day
progress["current_topic"] = topic

with open("data/progress.json", "w", encoding="utf-8") as f:
    json.dump(progress, f, indent=4)
print(f"✅ Lesson generated successfully!")
print(f"📚 Topic : {topic}")
print(f"📁 Saved : {output_file}")

git_commit_and_push(day - 1, topic)