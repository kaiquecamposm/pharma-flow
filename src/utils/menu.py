from rich.panel import Panel
from rich.prompt import Prompt

from core.commands.apply_stratification_in_patients import (
    apply_stratification_in_patients_command,
)
from core.commands.detected_outliers_in_clinical_data import (
    detected_outliers_in_clinical_data_command,
)
from core.commands.detected_outliers_in_production_data import (
    detected_outliers_in_production_data_command,
)
from core.commands.get_profile import get_profile_command
from core.commands.register_clinical_data import register_clinical_data_command
from core.commands.register_lote import register_lote_command
from core.commands.register_patient import register_patient_command
from core.commands.register_user import register_user_command
from core.commands.view_all_lotes_and_indicators_command import (
    view_all_lotes_and_indicators_command,
)
from core.commands.view_clinical_data import view_clinical_data_command
from core.entities.user import User
from utils import console
from utils.clear_terminal import clear


def patients_menu():
    console.io.print(Panel.fit("[bold cyan]🛠️  PATIENTS MENU[/bold cyan]", border_style="bright_magenta"))

    console.io.print("[bold]1.[/bold] Register Patient")
    console.io.print("[bold]2.[/bold] Back to Main Menu")

    choice = Prompt.ask("\n[bold]Choose an option[/bold]")
    clear()

    match choice:
        case "1":
            register_patient_command()
        case "2":
            return
        case _:
            console.io.print("[bold red]Invalid option. Please try again.[/bold red]")

def users_menu(user: User):
    console.io.print(Panel.fit("[bold cyan]🛠️  USERS MENU[/bold cyan]", border_style="bright_magenta"))

    console.io.print("[bold]1.[/bold] View Profile")
    console.io.print("[bold]2.[/bold] Register User")
    console.io.print("[bold]3.[/bold] Back to Main Menu")

    choice = Prompt.ask("\n[bold]Choose an option[/bold]")
    clear()

    match choice:
        case "1":
            get_profile_command(user.id)
        case "2":
            register_user_command()
        case "3":
            return
        case _:
            console.io.print("[bold red]Invalid option. Please try again.[/bold red]")

def clinical_data_menu(user: User):
    console.io.print(Panel.fit("[bold cyan]🛠️  CLINICAL DATA MENU[/bold cyan]", border_style="bright_magenta"))

    console.io.print("[bold]1.[/bold] Register Clinical Data")
    console.io.print("[bold]2.[/bold] View Clinical Data")
    console.io.print("[bold]3.[/bold] Back to Main Menu")

    choice = Prompt.ask("\n[bold]Choose an option[/bold]")
    clear()

    match choice:
        case "1":
            register_clinical_data_command(user.id)
        case "2":
            view_clinical_data_command()
        case "3":
            return
        case _:
            console.io.print("[bold red]Invalid option. Please try again.[/bold red]")

def lotes_menu(user: User):
    console.io.print(Panel.fit("[bold cyan]🛠️  LOTES MENU[/bold cyan]", border_style="bright_magenta"))

    console.io.print("[bold]1.[/bold] Register Lote")
    console.io.print("[bold]2.[/bold] View Lotes and Indicators")
    console.io.print("[bold]3.[/bold] Back to Main Menu")

    choice = Prompt.ask("\n[bold]Choose an option[/bold]")
    clear()

    match choice:
        case "1":
            register_lote_command(user.id)
        case "2":
            view_all_lotes_and_indicators_command()
        case "3":
            return
        case _:
            console.io.print("[bold red]Invalid option. Please try again.[/bold red]")

def analysis_menu():
    console.io.print(Panel.fit("[bold cyan]🛠️  ANALYSIS MENU[/bold cyan]", border_style="bright_magenta"))

    console.io.print("[bold]1.[/bold] Stratification in Patients")
    console.io.print("[bold]2.[/bold] Detected Outliers in Clinical Data")
    console.io.print("[bold]3.[/bold] Detected Outliers in Production Data")
    console.io.print("[bold]4.[/bold] Back to Main Menu")

    choice = Prompt.ask("\n[bold]Choose an option[/bold]")
    clear()

    match choice:
        case "1":
            apply_stratification_in_patients_command()
        case "2":
            detected_outliers_in_clinical_data_command()
        case "3":
            detected_outliers_in_production_data_command()
        case "4":
            return
        case _:
            console.io.print("[bold red]Invalid option. Please try again.[/bold red]")