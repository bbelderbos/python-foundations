import tempfile
from pathlib import Path

import pytest
from typer.testing import CliRunner

from main import (
    JournalEntry,
    add_entry,
    app,
    load_entries,
    matches_query,
)


@pytest.fixture
def db_file():
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        yield Path(f.name)


@pytest.fixture
def runner():
    return CliRunner()


# --- carried from earlier weeks ---


def test_add_and_load(db_file):
    add_entry("Title", "Content", ["python"], db_file)
    entries = load_entries(db_file)
    assert len(entries) == 1
    assert entries[0].title == "Title"


def test_cli_add_with_flags(db_file, runner):
    result = runner.invoke(
        app,
        [
            "add",
            "--title",
            "CLI",
            "--content",
            "Body",
            "--tags",
            "a, b",
            "--db",
            str(db_file),
        ],
    )
    assert result.exit_code == 0
    assert "Entry saved" in result.output


# --- Week 3: search, filtering, limiting ---


def test_matches_query_title(db_file):
    entry = JournalEntry(title="Python Basics", content="Content", tags=["python"])
    assert matches_query(entry, "python")


def test_matches_query_case_insensitive():
    entry = JournalEntry(title="PYTHON Basics", content="Content", tags=[])
    assert matches_query(entry, "python")


def test_matches_query_content_and_tags():
    entry = JournalEntry(title="Entry", content="I love pytest", tags=["testing"])
    assert matches_query(entry, "pytest")
    assert matches_query(entry, "test")  # matches the tag
    assert not matches_query(entry, "nonexistent")


def test_cli_search(db_file, runner):
    add_entry("Python Tips", "Use list comprehensions", ["python"], db_file)
    add_entry("Rust Guide", "Ownership model", ["rust"], db_file)
    result = runner.invoke(app, ["search", "python", "--db", str(db_file)])
    assert result.exit_code == 0
    assert "Python Tips" in result.output
    assert "Rust Guide" not in result.output


def test_cli_search_no_results(db_file, runner):
    add_entry("Entry", "Content", ["tag"], db_file)
    result = runner.invoke(app, ["search", "nope", "--db", str(db_file)])
    assert result.exit_code == 0
    assert "no" in result.output.lower()


def test_cli_list_with_tag(db_file, runner):
    add_entry("Python Entry", "Content", ["python"], db_file)
    add_entry("Rust Entry", "Content", ["rust"], db_file)
    result = runner.invoke(app, ["list", "--tag", "python", "--db", str(db_file)])
    assert result.exit_code == 0
    assert "Python Entry" in result.output
    assert "Rust Entry" not in result.output


def test_cli_list_with_limit(db_file, runner):
    for title in ("First", "Second", "Third"):
        add_entry(title, "Content", [], db_file)
    result = runner.invoke(app, ["list", "--limit", "2", "--db", str(db_file)])
    assert result.exit_code == 0
    assert "Third" in result.output
    assert "Second" in result.output
    assert "First" not in result.output
