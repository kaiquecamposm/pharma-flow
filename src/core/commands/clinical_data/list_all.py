from time import sleep

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_list_all_clinical_data import (
    make_list_all_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear


@authorize("clinical_data")
def list_all_clinical_data_command(user: User):
    console.io.print("[bold cyan]--- View All Clinical Data ---[/bold cyan]\n")

    list_all_clinical_data_use_case = make_list_all_clinical_data_use_case()
    clinical_data = list_all_clinical_data_use_case.execute(user.id)

    if not clinical_data:
        console.io.print("[bold red]Failed to retrieve clinical data.[/bold red]")
        sleep(1)
        clear()
        return

    for idx, data in enumerate(clinical_data, start=1):
        if idx > 1:
            console.io.print("-" * 40)
        console.io.print(f"[bold]{idx}.[/bold] Patient ID: {data.patient_id}")
        console.io.print(f"Data Type: {data.data_type}")
        console.io.print(f"Unit: {data.unit}")
        console.io.print(f"Value: {data.value}")
        console.io.print(f"Description: {data.description}")
        console.io.print(f"Date Recorded: {data.timestamp}")

    complete_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if complete_prompt:
        return