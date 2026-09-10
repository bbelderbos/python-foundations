import json
import tempfile
from pathlib import Path

import pytest

from main import (
    MAX_CONTENT_LENGTH,
    MAX_TITLE_LENGTH,
    JournalEntry,
    add_entry,
    load_entries,
    save_entries,
)


@pytest.fixture
def db_file():
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        yield Path(f.name)


def test_create_valid_entry():
    entry = JournalEntry(title="Test Title", content="Test content")
    assert entry.title == "Test Title"
    assert entry.content == "Test content"
    assert entry.tags == []
    assert entry.date is not None


def test_create_entry_with_tags():
    entry = JournalEntry(
        title="Tagged Entry",
        content="Some content",
        tags=["python", "learning"],
    )
    assert entry.tags == ["python", "learning"]


def test_each_entry_gets_own_tag_list():
    entry1 = JournalEntry(title="First", content="Content")
    entry2 = JournalEntry(title="Second", content="Content")
    entry1.tags.append("python")
    assert entry2.tags == []


def test_each_entry_gets_own_date():
    entry1 = JournalEntry(title="First", content="Content")
    entry2 = JournalEntry(title="Second", content="Content")
    assert entry1.date != "" and entry2.date != ""


def test_title_too_long():
    with pytest.raises(ValueError):
        JournalEntry(title="T" * (MAX_TITLE_LENGTH + 1), content="Valid")


def test_empty_title():
    with pytest.raises(ValueError):
        JournalEntry(title="", content="Valid")


def test_content_too_long():
    with pytest.raises(ValueError):
        JournalEntry(title="Valid", content="C" * (MAX_CONTENT_LENGTH + 1))


def test_empty_content():
    with pytest.raises(ValueError):
        JournalEntry(title="Valid", content="")


def test_save_and_load_entries(db_file):
    entries = [
        JournalEntry(title="First", content="Content 1", tags=["tag1"]),
        JournalEntry(title="Second", content="Content 2", tags=["tag2"]),
    ]
    save_entries(entries, db_file)
    loaded = load_entries(db_file)
    assert len(loaded) == 2
    assert loaded[0].title == "First"
    assert loaded[1].title == "Second"
    assert loaded[0].tags == ["tag1"]


def test_load_entries_empty_file(db_file):
    assert load_entries(db_file) == []


def test_load_entries_nonexistent_file():
    assert load_entries(Path("nonexistent.json")) == []


def test_save_entries_creates_valid_json(db_file):
    entries = [JournalEntry(title="Test", content="Content")]
    save_entries(entries, db_file)
    with open(db_file) as f:
        data = json.load(f)
    assert isinstance(data, list)
    assert data[0]["title"] == "Test"
    assert data[0]["content"] == "Content"


def test_add_entry(db_file):
    add_entry("My Title", "My Content", ["python"], db_file)
    entries = load_entries(db_file)
    assert len(entries) == 1
    assert entries[0].title == "My Title"
    assert entries[0].tags == ["python"]


def test_add_multiple_entries(db_file):
    add_entry("First", "Content 1", ["tag1"], db_file)
    add_entry("Second", "Content 2", ["tag2"], db_file)
    entries = load_entries(db_file)
    assert len(entries) == 2
    assert entries[0].title == "First"
    assert entries[1].title == "Second"
