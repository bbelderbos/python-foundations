# Week 3: Features & Search

Lesson: https://belderbos.dev/foundations/#week-3

Add search, tag filtering, and limiting to the CLI. `main.py` carries the Week 1-2
solution; `matches_query` and the `--tag` / `--limit` logic are stubbed with TODOs.

```bash
uv sync
uv run pytest -v        # earlier tests pass; the Week 3 tests are red
# implement matches_query and the list filters in main.py
uv run pytest -v        # green
uv run ruff format .
uv run ruff check --fix .
```

Try it:

```bash
uv run main.py search python
uv run main.py list --tag python --limit 5
```

The solution is on the `solution` branch.
