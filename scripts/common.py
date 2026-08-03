import json
import os
import re
import sys

# Windows consoles default to cp1252, which cannot encode the emoji these
# scripts print — that raised UnicodeEncodeError and killed the run.
for _stream in (sys.stdout, sys.stderr):
    if hasattr(_stream, "reconfigure"):
        try:
            _stream.reconfigure(encoding="utf-8", errors="replace")
        except (AttributeError, ValueError, OSError):
            pass

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

CONFIG_DIR = os.path.join(BASE_DIR, "config")
GENERATED_DIR = os.path.join(BASE_DIR, "generated")

PROGRESS_FILE = os.path.join(BASE_DIR, "data", "progress.json")
SUBJECTS_FILE = os.path.join(CONFIG_DIR, "subjects.json")
README_FILE = os.path.join(BASE_DIR, "README.md")

# Subjects whose lesson folder differs from the subject name.
# "Node.js" would otherwise create a folder literally named "Node.js".
FOLDER_OVERRIDES = {
    "Node.js": "NodeJS",
}


def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def save_json(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
        f.write("\n")


def subject_slug(subject):
    """'Node.js' -> 'nodejs', 'LangChain' -> 'langchain'.

    Plain subject.lower() produced 'node.js' and looked for a
    'node.js_topics.json' that never existed.
    """
    return re.sub(r"[^a-z0-9]", "", subject.lower())


def topic_file(subject):
    return os.path.join(CONFIG_DIR, f"{subject_slug(subject)}_topics.json")


def lesson_dir(subject):
    return os.path.join(GENERATED_DIR, FOLDER_OVERRIDES.get(subject, subject))


def load_topics(subject):
    path = topic_file(subject)

    if not os.path.exists(path):
        return None

    return load_json(path)["topics"]


def safe_topic_name(topic):
    """Filename-safe form of a topic. Must stay stable: existing lesson
    files are matched back to topics through this."""
    safe = topic.replace(" ", "_")

    for char in '/\\:*?"<>|':
        safe = safe.replace(char, "")

    return safe


def lesson_exists(subject, topic):
    """True if any DayNNN_<topic>.md already exists for this topic."""
    folder = lesson_dir(subject)

    if not os.path.isdir(folder):
        return False

    target = safe_topic_name(topic)
    pattern = re.compile(rf"^Day\d+_{re.escape(target)}\.md$")

    return any(pattern.match(name) for name in os.listdir(folder))


def load_progress():
    progress = load_json(PROGRESS_FILE)

    progress.setdefault("subject", load_subjects()[0])
    progress.setdefault("completed", [])
    progress.setdefault("completed_subjects", [])
    progress.setdefault("current_topic", "")
    progress.setdefault("day", 1)

    return progress


def save_progress(progress):
    save_json(PROGRESS_FILE, progress)


def load_subjects():
    return load_json(SUBJECTS_FILE)["subjects"]


def reconcile_completed(progress):
    """Rebuild `completed` from the lessons actually on disk.

    progress.json is a generated state file that is also committed, so
    merge conflicts kept truncating it. Whenever the recorded list and
    the filesystem disagreed, finished topics got picked again. Disk is
    the source of truth: a topic counts as done only if its lesson exists.
    """
    subject = progress["subject"]
    topics = load_topics(subject)

    if topics is None:
        return progress, []

    actual = [t for t in topics if lesson_exists(subject, t)]
    dropped = [t for t in progress.get("completed", []) if t not in actual]

    progress["completed"] = actual
    progress["day"] = len(actual) + 1

    return progress, dropped
