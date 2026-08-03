# Daily AI Learning Documentation

Welcome to the documentation for **Daily AI Learning**.

This project is designed to generate one AI-powered programming lesson per day, store it under `generated/`, update the progress dashboard in `README.md`, and optionally commit the changes automatically.

## Getting started

- Install the package: `python -m pip install -e .`
- Configure your API key: set `OPENROUTER_API_KEY`
- Generate a lesson: `daily-ai generate`
- Regenerate the README: `daily-ai readme`
- Validate config: `daily-ai validate`

## Project structure

- `config/` — roadmap and topic lists
- `data/` — runtime progress state
- `generated/` — AI lesson content
- `src/daily_ai_learning/` — package source
- `docs/` — GitHub Pages documentation
