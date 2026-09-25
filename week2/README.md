# Week 2: CLI & Type Safety

Lesson: https://belderbos.dev/foundations/#week-2

Build in your own `dev-journal` repo, not in this folder: copy this week's tests into
your project and make them pass with your own code (copy the tests, not the code).
The commands below run this folder on its own.

Add a Typer CLI (`add` and `list`) on top of your Week 1 model and persistence. The Week 1
code is already in `main.py`; the two commands are stubbed with TODOs.

```bash
uv sync
uv run pytest -v        # Week 1 tests pass; the CLI tests are red
# implement add() and list_entries() in main.py
uv run pytest -v        # green
uv run ruff format .
uv run ruff check --fix .
```

Try it for real:

```bash
uv run main.py add --title "First entry" --content "Learned Typer" --tags "python"
uv run main.py list
```

The solution is on the `solution` branch if you get truly stuck.
