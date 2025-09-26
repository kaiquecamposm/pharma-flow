import base64
from time import sleep

from rich.prompt import Prompt

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_register_patient import (
    make_register_patient_use_case,
)
from utils import console, valid_email
from utils.clear_terminal import clear


@authorize("patients")
def register_patient_command(user: User):
    console.io.print("[bold cyan]--- Register Patient ---[/bold cyan]\n")

    full_name = Prompt.ask("[green]Full name[/green]").strip()
    email = Prompt.ask("[green]Email[/green]").strip()

    # Verify email format
    email_verified = valid_email.execute(email)

    dob = Prompt.ask("[green]Date of Birth (YYYY-MM-DD)[/green]").strip()
    gender = Prompt.ask("[green]Gender (M/F)[/green]").strip().upper()
    active = Prompt.ask("[green]Active (y/n)[/green]").strip().lower() == "y"
    
    # Encode email in base64
    email_b64 = base64.b64encode(email_verified.encode("utf-8")).decode("utf-8")

    register_patient_use_case = make_register_patient_use_case()
    patient = register_patient_use_case.execute({
        "user_id": user.id,
        "full_name": full_name,
        "email": email_b64,
        "dob": dob, 
        "gender": gender,
        "active": active,
    })

    if not patient:
        console.io.print("\n[bold red]Failed to register patient.[/bold red]")
        sleep(3)
        clear()
        return
    
    console.io.print("\n[bold green]Patient registered successfully.[/bold green]")
    sleep(1)
    clear()