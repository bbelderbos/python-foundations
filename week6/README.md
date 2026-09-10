# Dev Journal

A command-line journal for tracking what you learn. Add entries, tag them, search across
them, and list them in a formatted table.

This is the finished project from Week 6 of the free
[Python Foundations](https://belderbos.dev/foundations/#week-6) course. Everything works and
the tests pass, this week is about shipping: writing this README, the final verification
pass, and (optionally) publishing or extending it. Use it as the model for the README you
write for your own copy.

## Install

```bash
git clone git@github.com:bbelderbos/python-foundations.git
cd python-foundations/week6
uv sync
```

## Usage

```bash
uv run journal add --title "Learned uv" --content "One tool for everything" --tags "python"
uv run journal list
uv run journal list --tag python --limit 5
uv run journal search pytest
```

## Develop

```bash
uv run ruff format .
uv run ruff check .
uv run pytest --cov=journal --cov-report=term-missing
```

## Optional extensions

- Publish to PyPI so anyone can `uv tool install` it.
- Add a `--pdf` export of your entries.
- Put a small [NiceGUI](https://nicegui.io/) web page in front of the same `JournalDatabase`.

Course: https://belderbos.dev/foundations/
