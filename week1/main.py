from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path

# TODO: set the limits used by validation (see the Week 1 lesson).
MAX_TITLE_LENGTH = 0
MAX_CONTENT_LENGTH = 0


@dataclass
class JournalEntry:
    # TODO: add fields: title (str), content (str),
    #       tags (list[str], default_factory=list),
    #       date (str, default_factory generating an ISO timestamp).
    title: str = ""

    def __post_init__(self) -> None:
        # TODO: raise ValueError if title/content are empty or too long.
        ...


def save_entries(entries: list[JournalEntry], db_path: Path) -> None:
    # TODO: convert entries to dicts and write them to db_path as JSON.
    raise NotImplementedError


def load_entries(db_path: Path) -> list[JournalEntry]:
    # TODO: read JSON from db_path and rebuild JournalEntry objects.
    #       Return [] for a missing or empty file.
    raise NotImplementedError


def add_entry(title: str, content: str, tags: list[str], db_path: Path) -> None:
    # TODO: load existing entries, append a new one, save them back.
    raise NotImplementedError
