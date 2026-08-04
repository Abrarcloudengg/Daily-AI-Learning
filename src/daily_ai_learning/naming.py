"""Name normalisation shared by the config loader, the lesson library, and the
README renderer.

These helpers are the single source of truth for how a human-facing subject or
topic name maps onto the filesystem. They are pure functions with no I/O so the
mapping can be unit tested exhaustively.

Historically each caller re-implemented its own variant. ``subject.lower()``
turned ``"Node.js"`` into ``node.js``, which pointed at a topic file that never
existed and silently stalled the whole roadmap at that subject.
"""

from __future__ import annotations

import re

__all__ = [
    "FOLDER_OVERRIDES",
    "LESSON_FILENAME_PATTERN",
    "lesson_filename",
    "lesson_folder_name",
    "safe_topic_name",
    "subject_slug",
    "topic_filename",
]

#: Subjects whose lesson folder name differs from the subject name. Without an
#: override ``"Node.js"`` would create a directory literally called ``Node.js``,
#: which reads badly and confuses tooling that treats the suffix as a file type.
FOLDER_OVERRIDES: dict[str, str] = {
    "Node.js": "NodeJS",
    "C++": "CPP",
    "C#": "CSharp",
}

#: Matches ``Day007_Nested_If.md`` and captures the day number and topic stem.
LESSON_FILENAME_PATTERN = re.compile(r"^Day(?P<day>\d+)_(?P<stem>.+)\.md$")

_NON_SLUG_CHARS = re.compile(r"[^a-z0-9]")
_ILLEGAL_PATH_CHARS = str.maketrans(dict.fromkeys('/\\:*?"<>|', ""))
_WHITESPACE = re.compile(r"\s+")


def subject_slug(subject: str) -> str:
    """Return the lookup slug for a subject name.

    >>> subject_slug("Node.js")
    'nodejs'
    >>> subject_slug("C++")
    'c'
    >>> subject_slug("LangChain")
    'langchain'
    """
    return _NON_SLUG_CHARS.sub("", subject.lower())


def topic_filename(subject: str) -> str:
    """Return the topic file name for a subject, e.g. ``nodejs_topics.json``."""
    return f"{subject_slug(subject)}_topics.json"


def lesson_folder_name(subject: str) -> str:
    """Return the directory name that holds a subject's generated lessons."""
    return FOLDER_OVERRIDES.get(subject, subject)


def safe_topic_name(topic: str) -> str:
    """Return a filename-safe form of a topic name.

    The result must stay stable across releases: existing lesson files are
    matched back to topics through this function, so changing it would make the
    generator believe finished topics are unfinished and regenerate them.
    """
    collapsed = _WHITESPACE.sub(" ", topic).strip()
    return collapsed.replace(" ", "_").translate(_ILLEGAL_PATH_CHARS)


def lesson_filename(day: int, topic: str) -> str:
    """Return the canonical lesson file name, e.g. ``Day007_Nested_If.md``.

    Day numbers are zero padded to three digits so lexical sort matches
    chronological order for the first 999 lessons.
    """
    if day < 1:
        raise ValueError(f"day must be >= 1, got {day!r}")
    return f"Day{day:03d}_{safe_topic_name(topic)}.md"
