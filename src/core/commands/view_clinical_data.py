from time import sleep

from core.use_cases.factories import make_view_clinical_data_use_case
from utils import console
from utils.clear_terminal import clear


def view_clinical_data_command():
    console.io.print("[bold cyan]--- View Clinical Data ---[/bold cyan]\n")

    view_clinical_data_use_case = make_view_clinical_data_use_case.execute()
    clinical_data = view_clinical_data_use_case.execute()

    for idx, data in enumerate(clinical_data, start=1):
        console.io.print(f"[bold]{idx}.[/bold] Patient ID: {data.patient_id}")
        console.io.print(f"    Data Type: {data.data_type}")
        console.io.print(f"    Description: {data.value}")
        console.io.print(f"    Date Recorded: {data.timestamp}\n")
    
    continue_prompt = console.io.input("[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if continue_prompt:
        return

    if clinical_data:
        console.io.print("\n[bold green]Clinical data retrieved successfully.[/bold green]")
        sleep(1)
        clear()
    else:
        console.io.print("\n[bold red]Failed to retrieve clinical data.[/bold red]")
        sleep(3)
        clear()