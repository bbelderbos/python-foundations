import json
from dataclasses import asdict
from pathlib import Path

from .models import JournalEntry


class JournalDatabase:
    def __init__(self, db_path: Path):
        self.db_path = db_path

    def load_entries(self) -> list[JournalEntry]:
        # TODO: return [] for a missing or empty file; otherwise read the JSON
        #       and rebuild JournalEntry objects.
        raise NotImplementedError

    def save_entries(self, entries: list[JournalEntry]) -> None:
        # TODO: write the entries to self.db_path as JSON (use asdict).
        raise NotImplementedError

    def add_entry(self, title: str, content: str, tags: list[str]) -> None:
        # TODO: load, append a new JournalEntry, save.
        raise NotImplementedError

    @staticmethod
    def search_entries(
        entries: list[JournalEntry], query: str, titles_only: bool = False
    ) -> list[JournalEntry]:
        # TODO: case-insensitive match on title (and, unless titles_only,
        #       content and tags). Return the matching entries.
        raise NotImplementedError
