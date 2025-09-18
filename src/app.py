from time import sleep

from rich.panel import Panel
from rich.prompt import Prompt

from core.commands.login import login_command
from utils import console
from utils.clear_terminal import clear
from utils.menu import (
    analysis_menu,
    clinical_data_menu,
    lotes_menu,
    patients_menu,
    users_menu,
)


def main():
    user = login_command()

    roles = ["Researcher", "Lab Technician", "Auditor"]

    while True:
        if user.role_name == "Admin":
            console.io.print(Panel.fit("[bold cyan]🛠️  ADMIN MENU[/bold cyan]", border_style="bright_magenta"))

            console.io.print("[bold]1.[/bold] Users")
            console.io.print("[bold]2.[/bold] Patients")
            console.io.print("[bold]3.[/bold] Clinical Data")
            console.io.print("[bold]4.[/bold] Lotes")
            console.io.print("[bold]5.[/bold] Analysis")
            console.io.print("[bold]6.[/bold] Exit")

            choice = Prompt.ask("\n[bold]Choose an option[/bold]")
            clear()

            match choice:
                case "1":
                    users_menu(user)
                case "2":
                    patients_menu()
                case "3":
                    clinical_data_menu(user)
                case "4":
                    lotes_menu(user)
                case "5":
                    analysis_menu()
                case "6":
                    console.io.print("[bold green]Exiting...[/bold green]")
                    sleep(1)
                    clear()
                    break
                case _:
                    console.io.print("[bold red]Invalid option. Please try again.[/bold red]")

        elif user.role_name in roles:
            console.io.print(Panel.fit("[bold cyan]🛠️  USER MENU[/bold cyan]", border_style="bright_magenta"))

            console.io.print("[bold]1.[/bold] Patients")
            console.io.print("[bold]2.[/bold] Clinical Data")
            console.io.print("[bold]3.[/bold] Exit")

            choice = Prompt.ask("\n[bold]Choose an option[/bold]")
            clear()

            match choice:
                case "1":
                    patients_menu()
                case "2":
                    clinical_data_menu(user)
                case "3":
                    console.io.print("[bold green]Exiting...[/bold green]")
                    sleep(1)
                    clear()
                    break
                case _:
                    console.io.print("[bold red]Invalid option. Please try again.[/bold red]")

if __name__ == "__main__":
    import time

    start = time.perf_counter()
    main()
    elapsed = time.perf_counter() - start
    print(f"{__file__} executed in {elapsed:0.2f} seconds.")