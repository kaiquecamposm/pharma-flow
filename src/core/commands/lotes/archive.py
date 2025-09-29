from time import sleep

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_archive_lote import make_archive_lote_use_case
from core.use_cases.factories.make_list_all_lotes_and_indicators import (
    make_list_all_lotes_and_indicators_use_case,
)
from utils import console
from utils.clear_terminal import clear
from utils.selects import select_lote


@authorize("lotes")
def archive_lote_command(user: User):
    console.io.print("[bold cyan]--- Archive Lote ---[/bold cyan]\n")

    list_all_lotes_and_indicators = make_list_all_lotes_and_indicators_use_case()
    lotes_and_indicators = list_all_lotes_and_indicators.execute(user.id)

    lote_id = select_lote(lotes_and_indicators)

    archive_lote_use_case = make_archive_lote_use_case()
    archived_lote = archive_lote_use_case.execute(user.id, lote_id)

    if not archived_lote:
        console.io.print(f"[bold red]Failed to archive lote with ID: {lote_id}[/bold red]")
        return

    console.io.print(f"\n[bold green]Lote with ID: {lote_id} archived successfully![/bold green]")
    sleep(1)
    clear()