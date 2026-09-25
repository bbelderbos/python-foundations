# Ship Your First Python App

Starter code for the free [Python Foundations](https://belderbos.dev/foundations/) course:
learn the local Python development workflow (uv, git, testing, your first PR) by building
a command-line developer journal.

Build the journal in your own `dev-journal` repo (the lesson walks you through creating it
in Week 1), with one branch and pull request per week. This repo is where the tests come
from: each `weekN/` folder has that week's tests and stubbed code.

## How to use it

- Copy a week's tests into your own project when the lesson tells you to, then write the
  code that makes them pass.
- Don't copy a week's `main.py` over yours: your own code carries forward week to week.
- To try a week's folder on its own:

```bash
git clone git@github.com:bbelderbos/python-foundations.git
cd python-foundations/week2
uv sync
uv run pytest -v   # red at first: the stubs are waiting for code
```

## Branches

- `main`: starter skeletons (tests plus stubs to fill in)
- `solution`: the completed code for every week

Follow along: https://belderbos.dev/foundations/
