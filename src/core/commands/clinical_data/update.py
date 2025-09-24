import base64
from time import sleep

from rich.prompt import Prompt

from core.entities.audit_log import AuditLog
from core.entities.clinical_data import ClinicalData
from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_list_clinical_data_by_patient_id import (
    make_list_clinical_data_by_patient_id_use_case,
)
from core.use_cases.factories.make_list_patients import make_list_patients_use_case
from core.use_cases.factories.make_update_clinical_data import (
    make_update_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear


def select_patient() -> str:
    list_patients_use_case = make_list_patients_use_case()
    patients = list_patients_use_case.execute()

    if not patients:
        console.io.print("\n[bold red]No patients found. Please register a patient first.[/bold red]")
        sleep(3)
        clear()
        return None
    
    console.io.print("[bold cyan]Select a patient to update clinical data:[/bold cyan]")
    for idx, patient in enumerate(patients, start=1):
        email_decoded = base64.b64decode(patient.email).decode("utf-8")
        console.io.print(f"[green]{idx}.[/green] {patient.full_name} - {email_decoded}")

    choice = Prompt.ask("\nEnter the number of the patient", choices=[str(i) for i in range(1, len(patients) + 1)])

    clear()

    return patients[int(choice) - 1].id

def select_clinical_data(patient_id: str) -> ClinicalData:
    list_clinical_data_by_patient_id_use_case = make_list_clinical_data_by_patient_id_use_case()
    clinical_data = list_clinical_data_by_patient_id_use_case.execute(patient_id)

    if not clinical_data:
        console.io.print("\n[bold red]No clinical data found for this patient. Please register clinical data first.[/bold red]")
        sleep(3)
        clear()
        return None
    
    console.io.print("\n[bold cyan]Select clinical data to update:[/bold cyan]")
    for idx, data in enumerate(clinical_data, start=1):
        console.io.print(f"[green]{idx}.[/green] {data.timestamp.format()} | {data.data_type} - {data.value} {data.unit} - {data.description}")

    choice = Prompt.ask("\nEnter the number of the clinical data", choices=[str(i) for i in range(1, len(clinical_data) + 1)])

    clear()

    return clinical_data[int(choice) - 1]

@authorize("clinical_data")
def update_clinical_data_command(user: User):
    console.io.print("[bold cyan]--- Update Clinical Data ---[/bold cyan]\n")

    patient_id = select_patient()
    clinical_data = select_clinical_data(patient_id)

    if not patient_id or not clinical_data:
        return

    console.io.print("\n[bold cyan]Enter new clinical data details:[/bold cyan]")

    data_type = Prompt.ask("Data Type", default=clinical_data.data_type)
    value = Prompt.ask("Value", default=clinical_data.value)
    unit = Prompt.ask("Unit", default=clinical_data.unit)
    description = Prompt.ask("Description", default=clinical_data.description)

    update_clinical_data_use_case = make_update_clinical_data_use_case()
    clinical_data_updated = update_clinical_data_use_case.execute(patient_id, clinical_data.id, user.id, data_type, value, unit, description)

    create_audit_log_use_case = make_create_audit_log_use_case()
    create_audit_log_use_case.execute(AuditLog(
        user_id=user.id,
        action="UPDATE_CLINICAL_DATA",
        target_id=patient_id if patient_id else "N/A",
        target_type="Patient, ClinicalData",
        details=f"Updated clinical data for patient: {patient_id}",
    ))

    if clinical_data_updated:
        console.io.print("\n[bold green]Clinical data updated successfully.[/bold green]")
        sleep(1)
        clear()
        return
    else:
        console.io.print("\n[bold red]Failed to update clinical datas.[/bold red]")
        sleep(3)
        clear()
        return