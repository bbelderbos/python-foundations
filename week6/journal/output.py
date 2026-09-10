from rich.console import Console
from rich.table import Table

from .models import JournalEntry

console = Console()


def list_entries(entries: list[JournalEntry]) -> None:
    if not entries:
        console.print("No journal entries found.")
        return
    table = Table(show_header=True, header_style="bold magenta")
    table.add_column("Date", style="dim")
    table.add_column("Note")
    table.add_column("Tags", style="italic yellow")
    for entry in entries:
        table.add_row(
            entry.date[:16],
            f"[bold]{entry.title}[/bold]\n{entry.content}",
            ", ".join(entry.tags),
        )
    console.print(table)
