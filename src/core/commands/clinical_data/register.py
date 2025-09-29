from time import sleep

from rich.prompt import Prompt

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_list_patients import make_list_patients_use_case
from core.use_cases.factories.make_register_clinical_data import (
    make_register_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear
from utils.selects import select_data_type, select_patient


@authorize("clinical_data")
def register_clinical_data_command(user: User):
    list_patients_use_case = make_list_patients_use_case()
    patients = list_patients_use_case.execute(user.id)

    if not patients:
        console.io.print("[bold yellow]No patients found. Please register a patient first.[/bold yellow]")
        sleep(1)
        clear()
        return
    
    patient_id = select_patient(patients)
    data_type = select_data_type()

    console.io.print("[bold cyan]--- Register Clinical Data ---[/bold cyan]\n")

    value = Prompt.ask(f"[green]Enter the value for {data_type['type']} ({data_type['unit']})[green]").strip()
    description = Prompt.ask("[green]Description[/green]").strip()

    register_clinical_data_use_case = make_register_clinical_data_use_case()
    clinical_data = register_clinical_data_use_case.execute(data_type["type"], value, data_type["unit"], description, user.id, patient_id)

    if not clinical_data:
        console.io.print("\n[bold red]Failed to register clinical data.[/bold red]")
        sleep(1)
        clear()
        return
    
    console.io.print("\n[bold green]Clinical data registered successfully.[/bold green]")
    sleep(1)
    clear()
    return