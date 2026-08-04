[← Docs home](index.md)

# Curriculum

The roadmap is data, not code. Two kinds of file.

## `config/subjects.json`

An ordered list. Subjects are worked through top to bottom; the generator only
moves on once every topic in the current subject has a lesson on disk.

```json
{
  "subjects": ["Python", "JavaScript", "HTML", "CSS", "..."]
}
```

## `config/topics/<slug>_topics.json`

One per subject. The slug is the subject lowercased with every non-alphanumeric
character removed — `Node.js` → `nodejs`, `C++` → `c`.

```json
{
  "subject": "Python",
  "topics": [
    "Introduction to Python",
    "Installing Python",
    "Variables and Data Types"
  ]
}
```

The `subject` field must match `subjects.json` exactly. `daily-ai validate`
warns when it does not, because a mismatch is almost always a copy-paste
accident — which is exactly how `dsa_topics.json` spent a while being a
verbatim copy of the Node.js topic list.

Topic order is lesson order. Put fundamentals first.

## Adding a subject

1. Append the name to `config/subjects.json`.
2. Create `config/topics/<slug>_topics.json` with a matching `subject` field.
3. If the name is not a legal folder name on Windows, add it to
   `FOLDER_OVERRIDES` in `src/daily_ai_learning/naming.py`:

   ```python
   FOLDER_OVERRIDES = {"Node.js": "NodeJS", "C++": "CPP", "C#": "CSharp"}
   ```

4. Run `daily-ai validate`, then `daily-ai readme` to refresh the dashboard.

## What `validate` checks

| Check | Severity |
| --- | --- |
| Subject listed but no topic file | error |
| Topic file is not an object, or `topics` is not a list of non-empty strings | error |
| Duplicate subject names | error |
| Two subjects whose slugs collide (they would share one topic file) | error |
| Declared `subject` disagrees with `subjects.json` | warning |
| **Two subjects with an identical topic list** | warning |
| Fewer than five topics | warning |

Errors exit 65. Warnings exit 0 but are worth reading.

## Where lessons land

```
generated/
├── Python/
│   ├── Day001_Introduction_to_Python.md
│   └── Day002_Installing_Python.md
└── NodeJS/
    └── Day046_Introduction_to_Node.md
```

The day number is global across the whole roadmap, not per subject, so the
sequence reads as one continuous course.

## Editing lessons

Editing a generated lesson is fine — the reconciler only cares that a file with
the right name exists, never about its contents.

Deleting one is also fine: the next run notices it is missing and regenerates
that exact topic. That is the intended way to redo a lesson you were not happy
with.

Renaming one is not fine. The filename is how completion is tracked, so a
renamed lesson looks like a deleted lesson plus an unrelated file.

## Reordering or removing topics

Both are safe. Completion is matched on the topic name embedded in the filename,
not on position, so inserting a topic in the middle does not invalidate anything
after it. The day numbers of *future* lessons shift; already-written files keep
their original numbers.

Removing a topic leaves its lesson file on disk as an orphan. Delete it by hand
if you want it gone.
