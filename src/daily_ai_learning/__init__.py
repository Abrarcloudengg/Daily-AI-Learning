"""Daily AI Learning — an autonomous curriculum generator.

The package turns a static curriculum (``config/subjects.json`` plus one topic
file per subject) into a growing library of Markdown lessons under
``generated/``. It is designed to run unattended from GitHub Actions, so every
component is written to fail loudly, resume safely, and never duplicate work.

Public entry points:

* :func:`daily_ai_learning.cli.main` — command line interface.
* :class:`daily_ai_learning.pipeline.LessonPipeline` — programmatic API.
"""

from __future__ import annotations

__all__ = ["__version__"]

__version__ = "2.0.0"
