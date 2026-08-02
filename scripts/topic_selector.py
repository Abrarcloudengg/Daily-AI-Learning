import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROGRESS_FILE = os.path.join(BASE_DIR, "data", "progress.json")


def load_progress():
    with open(PROGRESS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_progress(progress):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=4)


def get_next_topic():

    progress = load_progress()

    subject = progress["subject"]

    topic_file = os.path.join(
        BASE_DIR,
        "config",
        f"{subject.lower()}_topics.json"
    )

    with open(topic_file, "r", encoding="utf-8") as f:
        topic_data = json.load(f)

    topics = topic_data["topics"]

    completed = progress["completed"]

    for topic in topics:

        if topic not in completed:

            completed.append(topic)

            progress["completed"] = completed
            progress["current_topic"] = topic
            progress["day"] += 1

            save_progress(progress)

            return subject, topic

    return None, None