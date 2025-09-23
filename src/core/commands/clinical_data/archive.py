from time import sleep

from core.entities.audit_log import AuditLog
from core.use_cases.factories.make_archive_clinical_data import (
    make_archive_clinical_data_use_case,
)
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_list_all_clinical_data import (
    make_list_all_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear


def select_clinical_data():
    list_all_clinical_data_use_case = make_list_all_clinical_data_use_case()
    clinical_data = list_all_clinical_data_use_case.execute()

    if not clinical_data:
        console.io.print("[bold red]No clinical data found.[/bold red]")
        return None

    console.io.print("[bold cyan]Select a clinical data entry to archive:[/bold cyan]\n")
    for idx, data in enumerate(clinical_data, start=1):
        console.io.print(f"[bold white]{idx}.[/bold white] {data.id} - {data.data_type} ({data.value} {data.unit}) | {data.description}")

    while True:
        try:
            choice = int(console.io.input("\nEnter the number of the clinical data entry to archive: "))
            if 1 <= choice <= len(clinical_data):
                return clinical_data[choice - 1].id
            else:
                console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
        except ValueError:
            console.io.print("[bold red]Please enter a valid number.[/bold red]")

def archive_clinical_data_command(user_id: str):
    console.io.print("[bold cyan]--- Archive Clinical Data ---[/bold cyan]\n")

    clinical_data_id = select_clinical_data()

    archive_clinical_data_use_case = make_archive_clinical_data_use_case()
    archived_clinical_data = archive_clinical_data_use_case.execute(clinical_data_id)

    if not archived_clinical_data:
        console.io.print(f"[bold red]Failed to archive clinical data with ID: {clinical_data_id}[/bold red]")
        return
    
    create_audit_log_use_case = make_create_audit_log_use_case()
    create_audit_log_use_case.execute(AuditLog(
        user_id=user_id,
        action="ARCHIVE_CLINICAL_DATA",
        target_id=clinical_data_id,
        target_type="ClinicalData",
        details=f"Archived clinical data with ID: {clinical_data_id}",
    ))

    console.io.print(f"[bold green]Successfully archived clinical data with ID: {clinical_data_id}[/bold green]")
    sleep(2)
    clear()