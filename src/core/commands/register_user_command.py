import base64
import re
import time

from rich.prompt import Prompt

from core.entities.user import User
from core.use_cases.factories import make_register_user_use_case
from utils import console


def format_email(email: str) -> str:
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        console.io.print("[bold red]Invalid email format.[/bold red]")
        return
    
    return email

def select_role() -> str:
    console.io.print("[bold]Select role:[/bold]")

    roles = ["Researcher", "Lab Technician", "Auditor"]

    for idx, role in enumerate(roles, 1):
        console.io.print(f"[yellow]{idx}. {role}[/yellow]")
    role_choice = Prompt.ask("Enter the number for your role", choices=[str(i) for i in range(1, len(roles)+1)])
    try:
        role_idx = int(role_choice) - 1
        if role_idx < 0 or role_idx >= len(roles):
            console.io.print("[bold red]Invalid role selection.[/bold red]")
            return
        role_name = roles[role_idx]
    except ValueError:
        console.io.print("[bold red]Invalid input. Please enter a number.[/bold red]")
        console.io.clear()
        return
    
    return role_name

def execute():
    console.io.print("[bold cyan]--- Register User ---[/bold cyan]\n")

    email = Prompt.ask("[green]Email[/green]").strip()
    password = Prompt.ask("[green]Password[/green]", password=True).strip()
    full_name = Prompt.ask("[green]Full name[/green]").strip()
    role_name = select_role()
    active = Prompt.ask("[green]Active (y/n)[/green]").strip().lower() == "y"

    # Verify email format
    email_verified = format_email(email)

    # Encode full name and email in base64
    email_b64 = base64.b64encode(email_verified.encode("utf-8")).decode("utf-8")
    password_b64 = base64.b64encode(password.encode("utf-8")).decode("utf-8")

    user = User(
        email=email_b64,
        password=password_b64,
        full_name=full_name,
        role_name=role_name,
        active=active,
    )

    register_user_use_case = make_register_user_use_case.execute()
    user = register_user_use_case.execute(user)

    if user:
        console.io.print("[bold green]User registered successfully.[/bold green]")
        time.sleep(1)
        console.io.clear()
    else:
        console.io.print("[bold red]Failed to register user.[/bold red]")
        time.sleep(3)
        console.io.clear()