# Python Foundations

Starter code for the free [Python Foundations](https://belderbos.dev/foundations/) course:
learn the local Python development workflow (uv, git, testing, your first PR) by building
a command-line developer journal.

Each `weekN/` folder is a small standalone project with the tests for that week and a
starter file with the functions stubbed out. Your job is to make the tests pass. Work
through the matching lesson at https://belderbos.dev/foundations/

## Getting started

```bash
git clone git@github.com:bbelderbos/python-foundations.git
cd python-foundations/week1
uv sync
uv run pytest -v   # red at first: now make them green
```

## Branches

- `main` — starter skeletons (tests plus stubs to fill in)
- `solution` — the completed code for every week

Follow along: https://belderbos.dev/foundations/
