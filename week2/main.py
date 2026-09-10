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
    title: str = typer.Option(None, prompt="Title"),
    content: str = typer.Option(None, prompt="Content"),
    tags: str = typer.Option(None, prompt="Tags (comma separated)"),
    db: Path = typer.Option(Path("journal.json"), hidden=True),
) -> None:
    # TODO: parse tags into a list, call add_entry inside a try/except,
    #       echo "Entry saved." on success, raise typer.BadParameter on ValueError.
    raise NotImplementedError


@app.command("list")
def list_entries(
    db: Path = typer.Option(Path("journal.json"), hidden=True),
) -> None:
    # TODO: load entries; if none, echo a message containing "no";
    #       otherwise echo each entry's title, date, content, and tags.
    raise NotImplementedError


if __name__ == "__main__":
    app()
