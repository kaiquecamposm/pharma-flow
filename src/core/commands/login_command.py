import time

from rich.panel import Panel
from rich.prompt import Prompt

from core.use_cases.factories import make_verify_credentials_use_case
from utils import console


def execute():
    console.io.print(Panel.fit("[bold cyan]🔐 LOGIN SYSTEM[/bold cyan]", border_style="bright_magenta"))

    email = Prompt.ask("[green]Email[/green]")
    password = Prompt.ask("[green]Password[/green]", password=True)
    
    verify_credentials_use_case = make_verify_credentials_use_case.execute()
    professional = verify_credentials_use_case.execute(email, password)

    is_authenticated = professional is not None
    
    if is_authenticated:
        console.io.print(f"\n[bold green]Welcome, {professional.full_name}![/bold green]\n")
        time.sleep(1)
        console.io.clear()

        return professional.role_name
    else:
        console.io.print("\n[bold red]Invalid credentials. Please try again.[/bold red]")
        time.sleep(3)
        console.io.clear()

        return False