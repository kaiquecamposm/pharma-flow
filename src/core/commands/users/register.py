import base64
from time import sleep

from rich.prompt import Prompt

from core.entities.user import User
from core.use_cases.factories.make_register_user import make_register_user_use_case
from utils import console, valid_email
from utils.clear_terminal import clear
from utils.selects import select_role


def register_user_command(user: User):
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
    user = register_user_use_case.execute(user.id, email_b64, password_b64, full_name, role_name, active)

    if not user:
        console.io.print("\n[bold red]Failed to register user.[/bold red]")
        sleep(1)
        clear()
        return
    
    console.io.print("\n[bold green]User registered successfully.[/bold green]")
    sleep(1)
    clear()
    return