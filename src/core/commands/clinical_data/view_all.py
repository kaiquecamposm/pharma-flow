from time import sleep

from core.entities.audit_log import AuditLog
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_view_all_clinical_data import (
    make_view_all_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear


def view_all_clinical_data_command(user_id: str):
    console.io.print("[bold cyan]--- View All Clinical Data ---[/bold cyan]\n")

    view_all_clinical_data_use_case = make_view_all_clinical_data_use_case()
    clinical_data = view_all_clinical_data_use_case.execute()

    create_audit_log_use_case = make_create_audit_log_use_case()
    create_audit_log_use_case.execute(AuditLog(
        user_id=user_id,
        action="VIEW_ALL_CLINICAL_DATA",
        target_id="*MULTIPLE*",
        target_type="CLINICAL_DATA",
        details="User viewed all clinical data records.",
    ))

    if clinical_data:
        for idx, data in enumerate(clinical_data, start=1):
            if idx > 1:
                console.io.print("-" * 40)
            console.io.print(f"[bold]{idx}.[/bold] Patient ID: {data.patient_id}")
            console.io.print(f"Data Type: {data.data_type}")
            console.io.print(f"Unit: {data.unit}")
            console.io.print(f"Value: {data.value}")
            console.io.print(f"Description: {data.description}")
            console.io.print(f"Date Recorded: {data.timestamp}")
    else:
        raise ValueError(console.io.print("\n[bold red]Failed to retrieve clinical data.[/bold red]"))

    complete_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if complete_prompt:
        return