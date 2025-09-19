import base64
from time import sleep

from rich.prompt import Prompt

from core.constants.clinical_data_types import CLINICAL_DATA_TYPES
from core.entities.clinical_data import ClinicalData
from core.entities.patient import Patient
from core.use_cases.factories.make_list_patients import make_list_patients_use_case
from core.use_cases.factories.make_register_clinical_data import (
    make_register_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear


def select_patient(patients: list[Patient]):
    for idx, patient in enumerate(patients, start=1):
        email_decoded = base64.b64decode(patient.email).decode("utf-8")
        console.io.print(f"[bold]{idx}.[/bold] {email_decoded} - {patient.full_name} (ID: {patient.id})")

    choice = Prompt.ask("\n[bold]Choose a patient by number[/bold]")
    sleep(1)
    clear()

    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(patients):
            return patients[choice_idx].id
        else:
            console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
            return None
    except ValueError:
        console.io.print("[bold red]Invalid input. Please enter a number.[/bold red]")
        return None

def select_data_type():
    for idx, data_type in enumerate(CLINICAL_DATA_TYPES, start=1):
        console.io.print(f"[bold]{idx}.[/bold] {data_type['type']} ({data_type['unit']})")

    choice = Prompt.ask("\n[bold]Choose a data type by number[/bold]")
    sleep(1)
    clear()

    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(CLINICAL_DATA_TYPES):
            return CLINICAL_DATA_TYPES[choice_idx]
        else:
            console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
            return None
    except ValueError:
        console.io.print("[bold red]Invalid input. Please enter a number.[/bold red]")
        return None

def register_clinical_data_command(user_id: str = None):
    list_patients_use_case = make_list_patients_use_case()
    patients = list_patients_use_case.execute()

    if not patients:
        console.io.print("[bold yellow]No patients found. Please register a patient first.[/bold yellow]")
        sleep(2)
        clear()
        return
    
    patient_id = select_patient(patients)
    data_type = select_data_type()

    console.io.print("[bold cyan]--- Register Clinical Data ---[/bold cyan]\n")

    clinical_data = ClinicalData(
        patient_id=patient_id,
        data_type=data_type["type"],
        value=Prompt.ask(f"[green]Enter the value for {data_type['type']} ({data_type['unit']})[green]").strip(),
        unit=data_type["unit"],
        description=Prompt.ask("[green]Description[/green]").strip(),
        user_id=user_id
    )

    register_clinical_data_use_case = make_register_clinical_data_use_case()
    clinical_data = register_clinical_data_use_case.execute(clinical_data)

    if clinical_data:
        console.io.print("\n[bold green]Clinical data registered successfully.[/bold green]")
        sleep(1)
        clear()
        return
    else:
        console.io.print("\n[bold red]Failed to register clinical data.[/bold red]")
        sleep(2)
        clear()
        return