from time import sleep

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_archive_clinical_data import (
    make_archive_clinical_data_use_case,
)
from core.use_cases.factories.make_list_all_clinical_data import (
    make_list_all_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear
from utils.selects import select_clinical_data


@authorize("clinical_data")
def archive_clinical_data_command(user: User):
    console.io.print("[bold cyan]--- Archive Clinical Data ---[/bold cyan]\n")

    list_all_clinical_data_use_case = make_list_all_clinical_data_use_case()
    clinical_data = list_all_clinical_data_use_case.execute(user.id)

    clinical_data = select_clinical_data(clinical_data)

    if not clinical_data: 
        console.io.print("\n[bold red]No clinical data selected.[/bold red]")
        sleep(1)
        clear()
        return

    archive_clinical_data_use_case = make_archive_clinical_data_use_case()
    archived_clinical_data = archive_clinical_data_use_case.execute(user.id, clinical_data["id"])

    if not archived_clinical_data:
        console.io.print(f"[bold red]Failed to archive clinical data with ID: {clinical_data["id"]}[/bold red]")
        sleep(1)
        return

    console.io.print(f"[bold green]Successfully archived clinical data with ID: {clinical_data["id"]}[/bold green]")
    sleep(1)
    clear()