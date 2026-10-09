# Week 5: Testing & Polish

Lesson: https://belderbos.dev/foundations/#week-5

Move display into `src/journal/output.py` with a Rich table, then measure coverage. `output.py`
is stubbed; `cli.py` already calls it. Fill it in until the tests pass.

```bash
uv sync
uv run pytest -v        # red until output.list_entries is implemented
# fill in src/journal/output.py
uv run pytest -v        # green
uv run pytest --cov=journal --cov-report=term-missing   # check coverage
uv run ruff format .
uv run ruff check --fix .
```

The solution is on the `solution` branch.
