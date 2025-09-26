import base64
from time import sleep

from rich.prompt import Prompt

from core.use_cases.factories.make_register_user import make_register_user_use_case
from utils import console, valid_email
from utils.clear_terminal import clear


def select_role() -> str:
    console.io.print("[bold]Select role:[/bold]")

    ROLES = ["Researcher", "Lab Technician", "Auditor"]

    for idx, role in enumerate(ROLES, 1):
        console.io.print(f"[yellow]{idx}. {role}[/yellow]")

    role_choice = Prompt.ask("Enter the number for your role", choices=[str(i) for i in range(1, len(ROLES)+1)])

    try:
        role_idx = int(role_choice) - 1
        if role_idx < 0 or role_idx >= len(ROLES):
            console.io.print("\n[bold red]Invalid role selection.[/bold red]")
            return
        role_name = ROLES[role_idx]
    except ValueError:
        console.io.print("\n[bold red]Invalid input. Please enter a number.[/bold red]")
        clear()
        return
    
    return role_name

def register_user_command(user_id: int):
    console.io.print("[bold cyan]--- Register User ---[/bold cyan]\n")

    full_name = Prompt.ask("[green]Full name[/green]").strip()
    email = Prompt.ask("[green]Email[/green]").strip()

    # Verify email format
    email_verified = valid_email.execute(email)

    password = Prompt.ask("[green]Password[/green]", password=True).strip()
    role_name = select_role()
    active = Prompt.ask("[green]Active (y/n)[/green]").strip().lower() == "y"

    # Encode email and password in base64
    email_b64 = base64.b64encode(email_verified.encode("utf-8")).decode("utf-8")
    password_b64 = base64.b64encode(password.encode("utf-8")).decode("utf-8")

    register_user_use_case = make_register_user_use_case()
    user = register_user_use_case.execute(user_id, email_b64, password_b64, full_name, role_name, active)

    if not user:
        console.io.print("\n[bold red]Failed to register user.[/bold red]")
        sleep(3)
        clear()
        return
    
    console.io.print("\n[bold green]User registered successfully.[/bold green]")
    sleep(1)
    clear()
    return