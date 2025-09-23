import base64
from time import sleep

from rich.prompt import Prompt

from core.entities.audit_log import AuditLog
from core.entities.patient import Patient
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_register_patient import (
    make_register_patient_use_case,
)
from utils import console, valid_email
from utils.clear_terminal import clear


def register_patient_command(user_id: str):
    console.io.print("[bold cyan]--- Register Patient ---[/bold cyan]\n")

    full_name = Prompt.ask("[green]Full name[/green]").strip()
    email = Prompt.ask("[green]Email[/green]").strip()
    dob = Prompt.ask("[green]Date of Birth (YYYY-MM-DD)[/green]").strip()
    gender = Prompt.ask("[green]Gender (M/F)[/green]").strip().upper()
    active = Prompt.ask("[green]Active (y/n)[/green]").strip().lower() == "y"

    # Verify email format
    email_verified = valid_email.execute(email)
    
    # Encode email in base64
    email_b64 = base64.b64encode(email_verified.encode("utf-8")).decode("utf-8")

    patient = Patient(
        full_name=full_name,
        email=email_b64,
        dob=dob,
        gender=gender,
        active=active,
    )

    register_patient_use_case = make_register_patient_use_case()
    patient = register_patient_use_case.execute(patient)

    create_audit_log_use_case = make_create_audit_log_use_case()

    create_audit_log_use_case.execute(AuditLog(
        user_id=user_id,
        action="REGISTER_PATIENT",
        target_id=patient.id if patient else "N/A",
        target_type="Patient",
        details=f"Registered patient with email: {email_verified}",
    ))

    if patient:
        console.io.print("\n[bold green]Patient registered successfully.[/bold green]")
        sleep(1)
        clear()
        return
    else:
        console.io.print("\n[bold red]Failed to register patient.[/bold red]")
        sleep(3)
        clear()
        return