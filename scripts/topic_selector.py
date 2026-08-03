import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROGRESS_FILE = os.path.join(BASE_DIR, "data", "progress.json")
SUBJECTS_FILE = os.path.join(BASE_DIR, "config", "subjects.json")


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_progress(progress):
    with open(PROGRESS_FILE, "w", encoding="utf-8") as f:
        json.dump(progress, f, indent=4)


def get_next_topic():

    progress = load_json(PROGRESS_FILE)
    subjects = load_json(SUBJECTS_FILE)["subjects"]

    progress.setdefault("completed", [])
    progress.setdefault("completed_subjects", [])
    progress.setdefault("day", 1)

    subject = progress["subject"]

    if subject not in subjects:
        print(f"❌ Invalid subject: {subject}")
        return None, None

    while True:

        topic_file = os.path.join(
            BASE_DIR,
            "config",
            f"{subject.lower()}_topics.json"
        )

        if not os.path.exists(topic_file):
            print(f"❌ Topic file not found: {topic_file}")
            return None, None

        topics = load_json(topic_file)["topics"]

        for topic in topics:
            if topic not in progress["completed"]:
                return subject, topic

        # Subject completed
        if subject not in progress["completed_subjects"]:
            progress["completed_subjects"].append(subject)

        current_index = subjects.index(subject)

        # All subjects completed
        if current_index == len(subjects) - 1:
            save_progress(progress)
            return None, None

        # Switch to next subject
        subject = subjects[current_index + 1]

        progress["subject"] = subject
        progress["completed"] = []
        progress["current_topic"] = ""
        progress["day"] = 1

        save_progress(progress)