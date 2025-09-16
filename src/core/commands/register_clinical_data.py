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

data_types = [
    {
        "type": "Blood Pressure",
        "unit": "mmHg",
    },
    {
        "type": "Heart Rate",
        "unit": "bpm",
    },
    {
        "type": "Temperature",
        "unit": "°C",
    },
    {
        "type": "Respiratory Rate",
        "unit": "breaths/min",
    },
    {
        "type": "Oxygen Saturation",
        "unit": "%",
    },
    {
        "type": "Blood Glucose",
        "unit": "mg/dL",
    },
    {
        "type": "Cholesterol Levels",
        "unit": "mg/dL",
    },
    {
        "type": "Body Mass Index (BMI)",
        "unit": "kg/m²",
    },
    {
        "type": "Electrocardiogram (ECG) Results",
        "unit": "N/A",
    },
    {
        "type": "Allergy Information",
        "unit": "N/A",
    },
    {
        "type": "Medication List",
        "unit": "N/A",
    },
    {
        "type": "Immunization Records",
        "unit": "N/A",
    },
    {
        "type": "Smoking Status",
        "unit": "N/A",
    },
    {
        "type": "Alcohol Consumption",
        "unit": "N/A",
    },
    {
        "type": "Physical Activity Level",
        "unit": "N/A",
    },
    {
        "type": "Dietary Habits",
        "unit": "N/A",
    },
    {
        "type": "Sleep Patterns",
        "unit": "N/A",
    },
    {
        "type": "Mental Health Status",
        "unit": "N/A",
    },
    {
        "type": "Family Medical History",
        "unit": "N/A",
    },
    {
        "type": "Surgical History",
        "unit": "N/A",
    },
    {
        "type": "Laboratory Test Results",
        "unit": "N/A",
    },
    {
        "type": "Imaging Results (X-rays, MRIs, etc.)",
        "unit": "N/A",
    },
]

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
    for idx, data_type in enumerate(data_types, start=1):
        console.io.print(f"[bold]{idx}.[/bold] {data_type['type']} ({data_type['unit']})")

    choice = Prompt.ask("\n[bold]Choose a data type by number[/bold]")
    sleep(1)
    clear()

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
    list_patients_use_case = make_list_patients_use_case.execute()
    patients = list_patients_use_case.execute()

    if not patients:
        console.io.print("[bold yellow]No patients found. Please register a patient first.[/bold yellow]")
        sleep(3)
        clear()
        return
    
    patient_id = select_patient(patients)
    data_type = select_data_type()

    console.io.print("[bold cyan]--- Register Clinical Data ---[/bold cyan]\n")

    description = Prompt.ask("[green]Description[/green]").strip()

    clinical_data = ClinicalData(
        patient_id=patient_id,
        data_type=data_type["type"],
        value={
            "description": description,
            "unit": data_type["unit"],
        },
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