import base64
from time import sleep

from rich.prompt import Prompt

from core.entities.patient import Patient
from utils import console
from utils.clear_terminal import clear


def select_patient(patients: list[Patient]) -> str:
    if not patients:
        console.io.print("\n[bold red]No patients found. Please register a patient first.[/bold red]")
        sleep(3)
        clear()
        return None
    
    console.io.print("[bold cyan]Select a patient:[/bold cyan]")
    for idx, patient in enumerate(patients, start=1):
        email_decoded = base64.b64decode(patient.email).decode("utf-8")
        console.io.print(f"[bold]{idx}.[/bold] {email_decoded} - {patient.full_name} (ID: {patient.id})")

    choice = Prompt.ask("\nEnter the number of the patient", choices=[str(i) for i in range(1, len(patients) + 1)])

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

    