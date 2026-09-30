import json
from dataclasses import asdict, dataclass, field
from datetime import datetime
from pathlib import Path

import typer

MAX_TITLE_LENGTH = 50
MAX_CONTENT_LENGTH = 1000

app = typer.Typer()


@dataclass
class JournalEntry:
    title: str
    content: str
    tags: list[str] = field(default_factory=list)
    date: str = field(default_factory=lambda: datetime.now().isoformat())

    def __post_init__(self) -> None:
        if not self.title or len(self.title) > MAX_TITLE_LENGTH:
            raise ValueError(
                f"Title must be non-empty and <= {MAX_TITLE_LENGTH} characters"
            )
        if not self.content or len(self.content) > MAX_CONTENT_LENGTH:
            raise ValueError(
                f"Content must be non-empty and <= {MAX_CONTENT_LENGTH} characters"
            )


def save_entries(entries: list[JournalEntry], db_path: Path) -> None:
    data = [asdict(entry) for entry in entries]
    with open(db_path, "w") as f:
        json.dump(data, f, indent=2)


def load_entries(db_path: Path) -> list[JournalEntry]:
    if not db_path.exists() or db_path.stat().st_size == 0:
        return []
    with open(db_path) as f:
        data = json.load(f)
    return [JournalEntry(**entry) for entry in data]


def add_entry(title: str, content: str, tags: list[str], db_path: Path) -> None:
    entries = load_entries(db_path)
    entries.append(JournalEntry(title=title, content=content, tags=tags))
    save_entries(entries, db_path)


def matches_query(entry: JournalEntry, query: str) -> bool:
    q = query.lower()
    return (
        q in entry.title.lower()
        or q in entry.content.lower()
        or any(q in tag.lower() for tag in entry.tags)
    )


def _display(entry: JournalEntry) -> None:
    typer.echo(f"{entry.title} ({entry.date[:16]})")
    typer.echo(f"  {entry.content}")
    if entry.tags:
        typer.echo(f"  Tags: {', '.join(entry.tags)}")
    typer.echo()


@app.command()
def add(
    title: str = typer.Option("", prompt="Title"),
    content: str = typer.Option("", prompt="Content"),
    tags: str = typer.Option("", prompt="Tags (comma separated)"),
    db: Path = typer.Option(Path("journal.json"), hidden=True),
) -> None:
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []
    try:
        add_entry(title, content, tag_list, db)
        typer.echo("Entry saved.")
    except ValueError as e:
        raise typer.BadParameter(str(e)) from e


@app.command("list")
def list_entries(
    tag: list[str] = typer.Option([], help="Filter by tag (repeatable)"),
    limit: int = typer.Option(0, help="Show last N entries (0 = all)"),
    db: Path = typer.Option(Path("journal.json"), hidden=True),
) -> None:
    entries = load_entries(db)
    if tag:
        wanted = [t.lower() for t in tag]
        entries = [e for e in entries if any(et.lower() in wanted for et in e.tags)]
    if limit > 0:
        entries = entries[-limit:]
    if not entries:
        typer.echo("No journal entries found.")
        return
    for entry in entries:
        _display(entry)


@app.command()
def search(
    query: str = typer.Argument(..., help="Search term"),
    db: Path = typer.Option(Path("journal.json"), hidden=True),
) -> None:
    results = [e for e in load_entries(db) if matches_query(e, query)]
    if not results:
        typer.echo("No matching entries found.")
        return
    for entry in results:
        _display(entry)


if __name__ == "__main__":
    app()
