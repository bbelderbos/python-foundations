from rich.console import Console
from rich.table import Table

from .models import JournalEntry

console = Console()


def list_entries(entries: list[JournalEntry]) -> None:
    # TODO: if there are no entries, print "No journal entries found." and return.
    # TODO: otherwise build a rich Table with Date, Note, and Tags columns,
    #       add a row per entry (Note = title + content), and console.print it.
    raise NotImplementedError
