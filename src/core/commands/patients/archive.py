import base64
from time import sleep

from core.entities.audit_log import AuditLog
from core.use_cases.factories.make_archive_patient import make_archive_patient_use_case
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_list_patients import make_list_patients_use_case
from utils import console
from utils.clear_terminal import clear


def select_patient():
    list_patients_use_case = make_list_patients_use_case()
    patients = list_patients_use_case.execute()

    if not patients:
        console.io.print("[bold red]No patients found.[/bold red]")
        return None

    console.io.print("[bold cyan]Select a patient to archive:[/bold cyan]")
    for idx, patient in enumerate(patients, start=1):
        email_decoded = base64.b64decode(patient.email).decode("utf-8")
        console.io.print(f"[bold white]{idx}.[/bold white] {email_decoded} - {patient.full_name} (ID: {patient.id})")

    while True:
        try:
            choice = int(console.io.input("\nEnter the number of the patient to archive: "))
            if 1 <= choice <= len(patients):
                return patients[choice - 1].id
            else:
                console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
        except ValueError:
            console.io.print("[bold red]Please enter a valid number.[/bold red]")

def archive_patient_command(user_id: str):
    console.io.print("[bold cyan]--- Archive Patient ---[/bold cyan]\n")

    patient_id = select_patient()    

    archive_patient_use_case = make_archive_patient_use_case()
    archived_patient = archive_patient_use_case.execute(patient_id)

    if not archived_patient:
        console.io.print(f"[bold red]Failed to archive patient with ID: {patient_id}[/bold red]")
        return
    
    create_audit_log_use_case = make_create_audit_log_use_case()
    create_audit_log_use_case.execute(AuditLog(
        user_id=user_id,
        action="ARCHIVE_PATIENT",
        target_id=patient_id,
        target_type="Patient, ClinicalData",
        details=f"Archived patient with ID: {patient_id}",
    ))

    continue_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if continue_prompt:
        return