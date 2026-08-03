"""Prompt construction and lesson quality gates.

The lesson template lives here as data rather than inside an f-string, so the
same list drives the prompt sent to the model *and* the check that verifies
what came back. When a section is added, both sides update together.
"""

from __future__ import annotations

import re
from dataclasses import dataclass

__all__ = [
    "LESSON_SECTIONS",
    "SYSTEM_PROMPT",
    "QualityReport",
    "build_lesson_prompt",
    "inspect_lesson",
]

SYSTEM_PROMPT = (
    "You are a senior programming instructor and technical writer. "
    "You produce complete, accurate, beginner-to-advanced lessons in clean GitHub-flavoured Markdown. "
    "You never truncate a lesson, never emit placeholder text, and never wrap the whole document in a code fence."
)

#: Section headings every lesson must contain, in order. ``{topic}`` is
#: substituted with the lesson topic.
LESSON_SECTIONS: tuple[str, ...] = (
    "Learning Objectives",
    "Prerequisites",
    "What is {topic}?",
    "Why is it Important?",
    "Real World Analogy",
    "Theory",
    "Syntax",
    "Flow / Working",
    "Example 1 (Beginner)",
    "Example 2 (Intermediate)",
    "Example 3 (Advanced)",
    "Output",
    "Common Mistakes",
    "Best Practices",
    "Pro Tips",
    "Interview Questions (10)",
    "MCQs (10)",
    "Practice Questions (10)",
    "Coding Exercises (5)",
    "Mini Project",
    "Assignment",
    "Summary",
    "Key Takeaways",
    "Next Topic Preview",
)

_RULES = (
    "Return ONLY Markdown — no preamble, no sign-off, no surrounding code fence.",
    "Use every heading above, spelled exactly as shown, in the same order.",
    "Explain each concept from first principles before showing code.",
    "All code must be correct and runnable; show the real output.",
    "Use fenced code blocks with a language tag, and tables where they help.",
    "No placeholder text such as TODO, TBD, or `...`.",
    "Finish every section. Never stop mid-sentence.",
)

_HEADING = re.compile(r"^#{1,6}\s+(?P<title>.+?)\s*#*\s*$", re.MULTILINE)
_PLACEHOLDER = re.compile(r"\b(TODO|TBD|FIXME|Lorem ipsum|placeholder)\b", re.IGNORECASE)
_CODE_FENCE = re.compile(r"^```", re.MULTILINE)


def sections_for(topic: str) -> tuple[str, ...]:
    """Return the expected section titles for *topic*."""
    return tuple(section.format(topic=topic) for section in LESSON_SECTIONS)


def build_lesson_prompt(subject: str, topic: str, day: int) -> str:
    """Render the user prompt for one lesson.

    Args:
        subject: Subject being taught, e.g. ``"Python"``.
        topic: Topic for this lesson, e.g. ``"Decorators"``.
        day: One-based lesson number within the subject, shown to the model so
            it can pitch the difficulty.
    """
    outline = "\n\n".join(f"## {section}" for section in sections_for(topic))
    rules = "\n".join(f"- {rule}" for rule in _RULES)

    return (
        f"Write a complete, professional Markdown lesson.\n\n"
        f"Subject: {subject}\n"
        f"Topic: {topic}\n"
        f"Lesson number in this subject: {day}\n\n"
        f"Progress from beginner to intermediate to advanced within the lesson.\n\n"
        f"Use exactly this structure:\n\n"
        f"# {topic}\n\n"
        f"{outline}\n\n"
        f"Rules:\n\n{rules}\n"
    )


@dataclass(frozen=True)
class QualityReport:
    """Result of inspecting generated Markdown before it is written."""

    missing_sections: list[str]
    char_count: int
    truncated: bool
    has_placeholders: bool
    unbalanced_code_fence: bool
    suspicious_ending: bool

    @property
    def is_usable(self) -> bool:
        """Whether the lesson is good enough to keep.

        Missing sections and an odd-looking final character are tolerated:
        models reword headings, and a slightly imperfect lesson still beats no
        lesson at all. Truncation and an unclosed code fence are not tolerated,
        because both render as visibly broken Markdown on GitHub.
        """
        return not self.truncated and not self.unbalanced_code_fence

    def describe(self) -> list[str]:
        """Human-readable warnings, empty when the lesson is clean."""
        notes: list[str] = []
        if self.truncated:
            notes.append("the response was cut off by the token limit")
        if self.unbalanced_code_fence:
            notes.append("it contains an unclosed code fence")
        if self.suspicious_ending:
            notes.append("it does not end on sentence punctuation")
        if self.has_placeholders:
            notes.append("it contains placeholder text (TODO/TBD)")
        if self.missing_sections:
            preview = ", ".join(self.missing_sections[:5])
            suffix = f" (+{len(self.missing_sections) - 5} more)" if len(self.missing_sections) > 5 else ""
            notes.append(f"missing section(s): {preview}{suffix}")
        return notes


def inspect_lesson(
    content: str,
    topic: str,
    *,
    finish_reason: str | None = None,
    min_chars: int = 1200,
) -> QualityReport:
    """Check generated Markdown against the requested template.

    Args:
        content: The Markdown returned by the model.
        topic: Topic the lesson was requested for.
        finish_reason: Provider-reported stop reason; ``"length"`` means the
            token budget ran out mid-answer.
        min_chars: Below this the lesson is treated as truncated even when the
            provider claimed a clean stop.
    """
    text = content or ""
    present = {match.group("title").strip().lower() for match in _HEADING.finditer(text)}

    missing = [section for section in sections_for(topic) if section.strip().lower() not in present]

    stripped = text.strip()

    # `finish_reason == "length"` is the provider saying it ran out of budget
    # mid-sentence; a suspiciously short body means the same thing when the
    # provider does not report it.
    truncated = finish_reason == "length" or len(stripped) < min_chars

    # A finished lesson normally ends on prose, a list item, a table row, or a
    # closing code fence. Anything else is worth flagging but not rejecting.
    suspicious_ending = bool(stripped) and stripped[-1] not in ".!?:`|)]>_*\"'"

    return QualityReport(
        missing_sections=missing,
        char_count=len(stripped),
        truncated=truncated,
        has_placeholders=bool(_PLACEHOLDER.search(text)),
        unbalanced_code_fence=len(_CODE_FENCE.findall(text)) % 2 != 0,
        suspicious_ending=suspicious_ending,
    )
