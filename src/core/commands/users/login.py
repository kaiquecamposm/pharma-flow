from time import sleep

from rich.panel import Panel
from rich.prompt import Prompt

from core.use_cases.factories.make_verify_credentials import (
    make_verify_credentials_use_case,
)
from utils import console
from utils.clear_terminal import clear


def login_command():
    console.io.print(Panel.fit("[bold cyan]🔐 LOGIN SYSTEM[/bold cyan]", border_style="bright_magenta"))

    email = Prompt.ask("[green]Email[/green]")
    password = Prompt.ask("[green]Password[/green]", password=True)
    
    verify_credentials_use_case = make_verify_credentials_use_case()
    user = verify_credentials_use_case.execute(email, password)
    
    if not user:
        console.io.print("\n[bold red]Invalid credentials. Please try again.[/bold red]")
        sleep(1)
        clear()
        return

    console.io.print(f"\n[bold green]Welcome, {user.full_name}![/bold green]\n")
    sleep(1)
    clear()
    return user