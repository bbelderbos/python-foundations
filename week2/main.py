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
    entry = JournalEntry(title=title, content=content, tags=tags)
    entries.append(entry)
    save_entries(entries, db_path)


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
    db: Path = typer.Option(Path("journal.json"), hidden=True),
) -> None:
    entries = load_entries(db)
    if not entries:
        typer.echo("No journal entries found.")
        return
    for entry in entries:
        typer.echo(f"{entry.title} ({entry.date[:16]})")
        typer.echo(f"  {entry.content}")
        if entry.tags:
            typer.echo(f"  Tags: {', '.join(entry.tags)}")
        typer.echo()


if __name__ == "__main__":
    app()
