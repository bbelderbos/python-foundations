# Week 1: Project Setup & Data Model

Lesson: https://belderbos.dev/foundations/#week-1

Build the `JournalEntry` dataclass and the JSON persistence functions so the tests pass.

```bash
uv sync
uv run pytest -v        # red: 14 failing tests
# fill in main.py, one function at a time
uv run pytest -v        # green
uv run ruff format .
uv run ruff check --fix .
```

`main.py` has the function signatures stubbed with TODOs. Everything you need is in the
lesson. The solution lives on the `solution` branch if you get truly stuck, but try first.
