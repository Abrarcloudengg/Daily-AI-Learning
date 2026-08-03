from common import (
    load_progress,
    load_subjects,
    load_topics,
    lesson_exists,
    reconcile_completed,
    save_progress,
    topic_file,
)


def get_next_topic():
    """Return (subject, topic) for the next lesson, or (None, None) when
    the whole roadmap is finished."""

    progress = load_progress()
    subjects = load_subjects()

    subject = progress["subject"]

    if subject not in subjects:
        print(f"❌ Invalid subject: {subject}")
        return None, None

    progress, dropped = reconcile_completed(progress)

    if dropped:
        print(f"⚠ Recorded as done but no lesson file found: {', '.join(dropped)}")
        print("  These will be generated again.")

    while True:

        topics = load_topics(subject)

        if topics is None:
            print(f"❌ Topic file not found: {topic_file(subject)}")
            return None, None

        for topic in topics:
            if topic not in progress["completed"] and not lesson_exists(subject, topic):
                save_progress(progress)
                return subject, topic

        # Every topic in this subject is done.
        if subject not in progress["completed_subjects"]:
            progress["completed_subjects"].append(subject)

        current_index = subjects.index(subject)

        if current_index == len(subjects) - 1:
            save_progress(progress)
            return None, None

        subject = subjects[current_index + 1]

        progress["subject"] = subject
        progress["current_topic"] = ""

        # Start the new subject from whatever already exists on disk.
        progress, _ = reconcile_completed(progress)

        save_progress(progress)
