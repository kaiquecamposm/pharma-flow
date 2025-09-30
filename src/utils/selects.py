import base64
from time import sleep

from rich.prompt import Prompt

from core.constants.clinical_data_types import CLINICAL_DATA_TYPES
from core.entities.clinical_data import ClinicalData
from core.entities.patient import Patient
from utils import console
from utils.clear_terminal import clear


def select_data_type():
    for idx, data_type in enumerate(CLINICAL_DATA_TYPES, start=1):
        console.io.print(f"[bold]{idx}.[/bold] {data_type['type']} ({data_type['unit']})")

    try:
        choice = Prompt.ask("\n[bold]Choose a data type by number[/bold]")
        choice_idx = int(choice) - 1

        clear()
        if not 0 <= choice_idx < len(CLINICAL_DATA_TYPES):
            console.io.print("[bold red]Invalid choice. Please try again.[/bold red]") 
            sleep(1)
            return
        
        return CLINICAL_DATA_TYPES[choice_idx]
    except ValueError:
        raise ValueError("[bold red]Invalid input. Please enter a number.[/bold red]")

def select_clinical_data(clinical_data: list[ClinicalData]):
    if not clinical_data:
        console.io.print("[bold red]No clinical data found.[/bold red]")
        sleep(1)
        return

    console.io.print("[bold cyan]Select a clinical data:[/bold cyan]\n")
    for idx, data in enumerate(clinical_data, start=1):
        console.io.print(f"[bold white]{idx}.[/bold white] Patient: {data.patient_id} - {data.data_type} ({data.value} {data.unit}) | {data.description}")

    while True:
        try:
            choice = int(Prompt.ask("\nEnter the number of the clinical data: "))

            if not 1 <= choice <= len(clinical_data):
                console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
                sleep(1)
                return

            return clinical_data[choice - 1]
        except ValueError:
            raise ValueError("[bold red]Please enter a valid number.[/bold red]")

def select_patient(patients: list[Patient]) -> str:
    if not patients:
        console.io.print("\n[bold red]No patients found. Please register a patient first.[/bold red]")
        sleep(1)
        return

    console.io.print("[bold cyan]Select a patient:[/bold cyan]")
    for idx, patient in enumerate(patients, start=1):
        email_decoded = base64.b64decode(patient.email).decode("utf-8")
        console.io.print(f"[bold]{idx}.[/bold] {email_decoded} - {patient.full_name} (ID: {patient.id})")

    try:
        choice = Prompt.ask("\nEnter the number of the patient", choices=[str(i) for i in range(1, len(patients) + 1)])
        choice_idx = int(choice) - 1

        clear()
        if not 0 <= choice_idx < len(patients):
            console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")

        return patients[choice_idx].id
    except ValueError:
        raise ValueError("[bold red]Invalid input. Please enter a number.[/bold red]")

def select_lote(lotes_and_indicators: list):
    if not lotes_and_indicators:
        console.io.print("[bold red]No lotes found.[/bold red]")
        sleep(1)
        return

    console.io.print("[bold cyan]Select a lote:[/bold cyan]\n")
    for idx, lote in enumerate(lotes_and_indicators, start=1):
        console.io.print(f"[bold white]{idx}.[/bold white] {lote['product_name']} ({lote['lote_id']}) - {lote['quantity']} | {lote['start_date']} to {lote['end_date']}")

    while True:
        try:
            choice = int(console.io.input("\nEnter the number of the lote: "))

            clear()
            if not 1 <= choice <= len(lotes_and_indicators):
                console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
                sleep(1)
                return
            
            return lotes_and_indicators[choice - 1]["lote_id"] 
        except ValueError:
            raise ValueError("[bold red]Please enter a valid number.[/bold red]")

def select_role() -> str:
    console.io.print("[bold]Select role:[/bold]")

    ROLES = ["Researcher", "Lab Technician", "Auditor"]

    for idx, role in enumerate(ROLES, 1):
        console.io.print(f"[yellow]{idx}. {role}[/yellow]")

    try:
        role_choice = Prompt.ask("Enter the number for your role", choices=[str(i) for i in range(1, len(ROLES)+1)])
        role_idx = int(role_choice) - 1

        if not (role_idx > 0 or role_idx < len(ROLES)):
            console.io.print("\n[bold red]Invalid role selection.[/bold red]")

        role_name = ROLES[role_idx]

        return role_name
    except ValueError:
        raise ValueError("[bold red]Invalid input. Please enter a number.[/bold red]")