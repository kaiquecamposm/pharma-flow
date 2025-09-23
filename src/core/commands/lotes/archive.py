from time import sleep

from core.entities.audit_log import AuditLog
from core.use_cases.factories.make_archive_lote import make_archive_lote_use_case
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_list_all_lotes_and_indicators import (
    make_list_all_lotes_and_indicators_use_case,
)
from utils import console
from utils.clear_terminal import clear


def select_lote():
    list_all_lotes_and_indicators = make_list_all_lotes_and_indicators_use_case()
    lotes_and_indicators = list_all_lotes_and_indicators.execute()

    if not lotes_and_indicators:
        console.io.print("[bold red]No lotes found.[/bold red]")
        return None

    console.io.print("[bold cyan]Select a lote to archive:[/bold cyan]\n")
    for idx, lote in enumerate(lotes_and_indicators, start=1):
        console.io.print(f"[bold white]{idx}.[/bold white] {lote['product_name']} ({lote['lote_id']}) - {lote['quantity']} | {lote['start_date']} to {lote['end_date']}")

    while True:
        try:
            choice = int(console.io.input("\nEnter the number of the lote to archive: "))
            if 1 <= choice <= len(lotes_and_indicators):
                return lotes_and_indicators[choice - 1]["lote_id"]
            else:
                console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
        except ValueError:
            console.io.print("[bold red]Please enter a valid number.[/bold red]")

def archive_lote_command(user_id: str):
    console.io.print("[bold cyan]--- Archive Lote ---[/bold cyan]\n")

    lote_id = select_lote()

    archive_lote_use_case = make_archive_lote_use_case()
    archived_lote = archive_lote_use_case.execute(lote_id)

    if not archived_lote:
        console.io.print(f"[bold red]Failed to archive lote with ID: {lote_id}[/bold red]")
        return
    
    create_audit_log_use_case = make_create_audit_log_use_case()
    create_audit_log_use_case.execute(AuditLog(
        user_id=user_id,
        action="ARCHIVE_LOTE",
        target_id=lote_id,
        target_type="Lote, ProductionData",
        details=f"Lote {lote_id} archived successfully.",
    ))

    console.io.print(f"\n[bold green]Lote with ID: {lote_id} archived successfully![/bold green]")
    sleep(2)
    clear()