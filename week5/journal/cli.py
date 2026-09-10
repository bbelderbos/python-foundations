from pathlib import Path

import typer

from . import output
from .db import JournalDatabase

app = typer.Typer()

DEFAULT_DB = Path("journal.json")


@app.command()
def add(
    title: str = typer.Option(None, prompt="Title"),
    content: str = typer.Option(None, prompt="Content"),
    tags: str = typer.Option(None, prompt="Tags (comma separated)"),
    db: Path = typer.Option(DEFAULT_DB, hidden=True),
) -> None:
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []
    try:
        JournalDatabase(db).add_entry(title, content, tag_list)
        typer.echo("Entry saved.")
    except ValueError as e:
        raise typer.BadParameter(str(e))


@app.command("list")
def list_entries(
    tag: list[str] = typer.Option([], help="Filter by tag (repeatable)"),
    limit: int = typer.Option(0, help="Show last N entries (0 = all)"),
    db: Path = typer.Option(DEFAULT_DB, hidden=True),
) -> None:
    entries = JournalDatabase(db).load_entries()
    if tag:
        wanted = [t.lower() for t in tag]
        entries = [e for e in entries if any(et.lower() in wanted for et in e.tags)]
    if limit > 0:
        entries = entries[-limit:]
    output.list_entries(entries)


@app.command()
def search(
    query: str = typer.Argument(..., help="Search term"),
    db: Path = typer.Option(DEFAULT_DB, hidden=True),
) -> None:
    entries = JournalDatabase(db).load_entries()
    results = JournalDatabase.search_entries(entries, query)
    if not results:
        typer.echo("No matching entries found.")
        return
    output.list_entries(results)
