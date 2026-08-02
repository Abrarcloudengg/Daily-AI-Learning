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
    subjects_data = load_json(SUBJECTS_FILE)

    subjects = subjects_data["subjects"]

    while True:

        subject = progress["subject"]

        topic_file = os.path.join(
            BASE_DIR,
            "config",
            f"{subject.lower()}_topics.json"
        )

        topic_data = load_json(topic_file)

        topics = topic_data["topics"]

        completed = progress["completed"]

        # Next topic
        for topic in topics:

            if topic not in completed:

                completed.append(topic)

                progress["completed"] = completed
                progress["current_topic"] = topic
                progress["day"] += 1

                save_progress(progress)

                return subject, topic

        # Subject completed
        if subject not in progress["completed_subjects"]:
            progress["completed_subjects"].append(subject)

        current_index = subjects.index(subject)

        # All subjects completed
        if current_index + 1 >= len(subjects):

            save_progress(progress)
            return None, None

        # Switch subject
        next_subject = subjects[current_index + 1]

        progress["subject"] = next_subject
        progress["day"] = 0
        progress["current_topic"] = ""
        progress["completed"] = []

        save_progress(progress)