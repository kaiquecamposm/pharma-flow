from time import sleep

from core.use_cases.factories import make_get_profile_use_case
from utils import console
from utils.clear_terminal import clear


def get_profile_command(user_id: str):
    console.io.print("[bold cyan]--- My Profile ---[/bold cyan]\n")

    get_profile_use_case = make_get_profile_use_case.execute()
    profile = get_profile_use_case.execute(user_id)

    if profile:
        console.io.print(f"[bold green]ID:[/bold green] {profile.id}")
        console.io.print(f"[bold green]Full Name:[/bold green] {profile.full_name}")
        console.io.print(f"[bold green]Email:[/bold green] {profile.email.__len__() * '*'}")
        console.io.print(f"[bold green]Password:[/bold green] {profile.password.__len__() * '*'}")
        console.io.print(f"[bold green]Role:[/bold green] {profile.role_name}")
        console.io.print(f"[bold green]Active:[/bold green] {'Yes' if profile.active else 'No'}")
    else:
        console.io.print("[bold red]Profile not found.[/bold red]")
    
    console.io.print("\n")
    enter = console.io.input("Press [bold green]Enter[/bold green] to return to the menu...")
    sleep(1)
    clear()

    if enter:
        return