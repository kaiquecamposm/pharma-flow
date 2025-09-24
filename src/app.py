from time import sleep

from rich.panel import Panel
from rich.prompt import Prompt

from core.commands.users.login import login_command
from utils import console
from utils.clear_terminal import clear
from utils.menu import (
    analysis_menu,
    audit_menu,
    clinical_data_menu,
    education_menu,
    lotes_menu,
    patients_menu,
    users_menu,
)


def main():
    user = login_command()

    while True:
        console.io.print(Panel.fit("[bold cyan]🛠️  MENU[/bold cyan]", border_style="bright_magenta"))

        console.io.print("[bold]1.[/bold] Users")
        console.io.print("[bold]2.[/bold] Patients")
        console.io.print("[bold]3.[/bold] Clinical Data")
        console.io.print("[bold]4.[/bold] Lotes")
        console.io.print("[bold]5.[/bold] Analysis")
        console.io.print("[bold]6.[/bold] Education")
        console.io.print("[bold]7.[/bold] Audit")
        console.io.print("[bold]8.[/bold] Exit")

        choice = Prompt.ask("\n[bold]Choose an option[/bold]")
        clear()

        match choice:
            case "1":
                users_menu(user)
            case "2":
                patients_menu(user)
            case "3":
                clinical_data_menu(user)
            case "4":
                lotes_menu(user)
            case "5":
                analysis_menu(user)
            case "6":
                education_menu(user)
            case "7":
                audit_menu(user)
            case "8":
                console.io.print("[bold green]Exiting...[/bold green]")
                sleep(1)
                clear()
                break
            case _:
                console.io.print("[bold red]Invalid option. Please try again.[/bold red]")

if __name__ == "__main__":
    main()