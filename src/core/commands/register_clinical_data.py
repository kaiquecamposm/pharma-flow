import base64
from time import sleep

from rich.prompt import Prompt

from core.entities.clinical_data import ClinicalData
from core.entities.patient import Patient
from core.use_cases.factories import (
    make_list_patients_use_case,
    make_register_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear


def select_patient(patients: list[Patient]):
    console.io.print("[bold cyan]--- Select Patient ---[/bold cyan]\n")

    for idx, patient in enumerate(patients, start=1):
        email_decoded = base64.b64decode(patient.email).decode("utf-8")
        console.io.print(f"[bold]{idx}.[/bold] {email_decoded} - {patient.full_name} (ID: {patient.id})")

    choice = Prompt.ask("\n[bold]Choose a patient by number[/bold]")

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
    data_types = [
        "Blood Pressure",
        "Heart Rate",
        "Temperature",
        "Respiratory Rate",
        "Oxygen Saturation",
        "Blood Glucose",
        "Cholesterol Levels",
        "Body Mass Index (BMI)",
        "Electrocardiogram (ECG) Results",
        "Allergy Information",
        "Medication List",
        "Immunization Records",
        "Smoking Status",
        "Alcohol Consumption",
        "Physical Activity Level",
        "Dietary Habits",
        "Sleep Patterns",
        "Mental Health Status",
        "Family Medical History",
        "Surgical History",
        "Laboratory Test Results",
        "Imaging Results (X-rays, MRIs, etc.)",
    ]

    for idx, data_type in enumerate(data_types, start=1):
        console.io.print(f"[bold]{idx}.[/bold] {data_type}")

    choice = Prompt.ask("\n[bold]Choose a data type by number[/bold]")

    try:
        choice_idx = int(choice) - 1
        if 0 <= choice_idx < len(data_types):
            return data_types[choice_idx]
        else:
            console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
            return None
    except ValueError:
        console.io.print("[bold red]Invalid input. Please enter a number.[/bold red]")
        return None

def register_clinical_data_command():
    console.io.print("[bold cyan]--- Register Clinical Data ---[/bold cyan]\n")

    list_patients_use_case = make_list_patients_use_case.execute()
    patients = list_patients_use_case.execute()

    if not patients:
        console.io.print("[bold yellow]No patients found. Please register a patient first.[/bold yellow]")
        sleep(3)
        clear()
        return
    
    patient_id = select_patient(patients)
    data_type = Prompt.ask("[green]Data Type[/green]").strip()
    value = Prompt.ask("[green]Value[/green]").strip()
    active = Prompt.ask("[green]Active (y/n)[/green]").strip().lower() == "y"

    clinical_data = ClinicalData(
        patient_id=patient_id,
        data_type=data_type,
        value=value,
        active=active
    )

    register_clinical_data_use_case = make_register_clinical_data_use_case.execute()
    clinical_data = register_clinical_data_use_case.execute(clinical_data)

    if clinical_data:
        console.io.print("\n[bold green]Clinical data registered successfully.[/bold green]")
        sleep(1)
        clear()
    else:
        console.io.print("\n[bold red]Failed to register clinical data.[/bold red]")
        sleep(3)
        clear()