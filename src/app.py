from time import sleep

from rich.panel import Panel
from rich.prompt import Prompt

from core.commands.get_profile import get_profile_command
from core.commands.login import login_command
from core.commands.register_clinical_data import register_clinical_data_command
from core.commands.register_patient import register_patient_command
from core.commands.register_user import register_user_command
from core.commands.view_clinical_data import view_clinical_data_command
from utils import console
from utils.clear_terminal import clear


def main():
    user = login_command()

    roles = ["Researcher", "Lab Technician", "Auditor"]

    while True:
        if user.role_name == "Admin":
            console.io.print(Panel.fit("[bold cyan]🛠️  ADMIN MENU[/bold cyan]", border_style="bright_magenta"))

            console.io.print("[bold]1.[/bold] My Profile")
            console.io.print("[bold]2.[/bold] Register User")
            console.io.print("[bold]3.[/bold] Register Patient")
            console.io.print("[bold]4.[/bold] Register Clinical Data")
            console.io.print("[bold]5.[/bold] Register Production Data")
            console.io.print("[bold]6.[/bold] View Clinical Data")
            console.io.print("[bold]7.[/bold] Exit")

            choice = Prompt.ask("\n[bold]Choose an option[/bold]")
            clear()

            match choice:
                case "1":
                    get_profile_command(user.id)
                case "2":
                    register_user_command()
                case "3":
                    register_patient_command()
                case "4":
                    register_clinical_data_command(user.id)
                case "5":
                    console.io.print("[bold green]-- Register Production Data --[/bold green]")
                    sleep(1)
                    clear()
                case "6":
                    console.io.print("[bold green]-- Register Lote --[/bold green]")
                    sleep(1)
                    clear()
                case "7":
                    view_clinical_data_command()
                case "8":
                    console.io.print("[bold green]Exiting...[/bold green]")
                    sleep(1)
                    clear()
                    break
                case _:
                    console.io.print("[bold red]Invalid option. Please try again.[/bold red]")

        elif user.role_name in roles:
            console.io.print(Panel.fit("[bold cyan]🛠️  USER MENU[/bold cyan]", border_style="bright_magenta"))

            console.io.print("[bold]1.[/bold] My Profile")
            console.io.print("[bold]2.[/bold] Register Patient")
            console.io.print("[bold]3.[/bold] Register Clinical Data")
            console.io.print("[bold]4.[/bold] View Clinical Data")
            console.io.print("[bold]5.[/bold] Exit")

            choice = Prompt.ask("\n[bold]Choose an option[/bold]")
            clear()

            match choice:
                case "1":
                    get_profile_command(user.id)
                case "2":
                    register_patient_command()
                case "3":
                    register_clinical_data_command(user.id)
                case "4":
                    view_clinical_data_command()
                case "5":
                    console.io.print("[bold green]Exiting...[/bold green]")
                    sleep(1)
                    clear()
                    break
                case _:
                    console.io.print("[bold red]Invalid option. Please try again.[/bold red]")

if __name__ == "__main__":
    main()