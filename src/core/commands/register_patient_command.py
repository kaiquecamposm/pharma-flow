import base64
import re
import time

from rich.prompt import Prompt

from core.entities.patient import Patient
from core.entities.user import User
from core.use_cases.factories import make_register_user_use_case
from utils import console, valid_email


def execute():
    console.io.print("[bold cyan]--- Register Patient ---[/bold cyan]\n")

    full_name = Prompt.ask("[green]Full name[/green]").strip()
    email = Prompt.ask("[green]Email[/green]").strip()
    dob = Prompt.ask("[green]Date of Birth (YYYY-MM-DD)[/green]").strip()
    gender = Prompt.ask("[green]Gender (M/F)[/green]").strip().upper()
    active = Prompt.ask("[green]Active (y/n)[/green]").strip().lower() == "y"

    # Verify email format
    email_verified = valid_email.execute(email)

    patient = Patient(
        full_name=full_name,
        email=email_verified,
        dob=dob,
        gender=gender,
        clinical_history=None,
        active=active,
    )

    register_patient_use_case = make_register_user_use_case.execute()
    patient = register_patient_use_case.execute(patient)

    if patient:
        console.io.print("[bold green]Patient registered successfully.[/bold green]")
        time.sleep(1)
        console.io.clear()
    else:
        console.io.print("[bold red]Failed to register patient.[/bold red]")
        time.sleep(3)
        console.io.clear()