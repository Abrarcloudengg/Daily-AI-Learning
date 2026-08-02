import json


def get_next_topic():

    with open("config/python_topics.json", "r", encoding="utf-8") as f:
        topics = json.load(f)

    with open("data/progress.json", "r", encoding="utf-8") as f:
        progress = json.load(f)

    completed = progress["completed"]

    for topic in topics["topics"]:

        if topic not in completed:

            progress["current_topic"] = topic

            with open("data/progress.json", "w", encoding="utf-8") as p:
                json.dump(progress, p, indent=4)

            return topic

    return None