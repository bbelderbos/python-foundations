import json
from dataclasses import asdict
from pathlib import Path

from .models import JournalEntry


class JournalDatabase:
    def __init__(self, db_path: Path):
        self.db_path = db_path

    def load_entries(self) -> list[JournalEntry]:
        if not self.db_path.exists() or self.db_path.stat().st_size == 0:
            return []
        with open(self.db_path) as f:
            return [JournalEntry(**e) for e in json.load(f)]

    def save_entries(self, entries: list[JournalEntry]) -> None:
        with open(self.db_path, "w") as f:
            json.dump([asdict(e) for e in entries], f, indent=2)

    def add_entry(self, title: str, content: str, tags: list[str]) -> None:
        entries = self.load_entries()
        entries.append(JournalEntry(title=title, content=content, tags=tags))
        self.save_entries(entries)

    @staticmethod
    def search_entries(
        entries: list[JournalEntry], query: str, titles_only: bool = False
    ) -> list[JournalEntry]:
        q = query.lower()
        results = []
        for entry in entries:
            if titles_only:
                if q in entry.title.lower():
                    results.append(entry)
            elif (
                q in entry.title.lower()
                or q in entry.content.lower()
                or any(q in tag.lower() for tag in entry.tags)
            ):
                results.append(entry)
        return results
