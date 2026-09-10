import tempfile
from pathlib import Path

import pytest

from journal.db import JournalDatabase


@pytest.fixture
def db_file():
    with tempfile.NamedTemporaryFile(suffix=".json", delete=False) as f:
        yield Path(f.name)


@pytest.fixture
def db(db_file):
    return JournalDatabase(db_file)
