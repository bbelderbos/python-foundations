# Week 4: Code Organization & Testing

Lesson: https://belderbos.dev/foundations/#week-4

Build in your own `dev-journal` repo, not in this folder: copy this week's tests into
your project and make them pass with your own code (copy the tests, not the code).
The commands below run this folder on its own.

The single-file app is now a `journal/` package. `models.py` and `cli.py` are done; your
job is `journal/db.py`, the `JournalDatabase` class (methods are stubbed with TODOs). The
tests live in `tests/` with shared fixtures in `conftest.py`.

```bash
uv sync
uv run pytest -v        # red until JournalDatabase is implemented
# fill in journal/db.py
uv run pytest -v        # green
uv run ruff format .
uv run ruff check --fix .
uv run journal --help   # the entry point works once the package installs
```

The solution is on the `solution` branch.
