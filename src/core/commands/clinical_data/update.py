from time import sleep

from rich.prompt import Prompt

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_list_clinical_data_by_patient_id import (
    make_list_clinical_data_by_patient_id_use_case,
)
from core.use_cases.factories.make_list_patients import make_list_patients_use_case
from core.use_cases.factories.make_update_clinical_data import (
    make_update_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear
from utils.select_clinical_data import select_clinical_data
from utils.select_patient import select_patient


@authorize("clinical_data")
def update_clinical_data_command(user: User):
    console.io.print("[bold cyan]--- Update Clinical Data ---[/bold cyan]\n")

    list_patients_use_case = make_list_patients_use_case()
    patients = list_patients_use_case.execute(user.id)

    patient_id = select_patient(patients)

    list_clinical_data_by_patient_id_use_case = make_list_clinical_data_by_patient_id_use_case()
    clinical_data = list_clinical_data_by_patient_id_use_case.execute(user.id, patient_id)

    clinical_data = select_clinical_data(clinical_data)

    if not patient_id or not clinical_data:
        return

    console.io.print("\n[bold cyan]Enter new clinical data details:[/bold cyan]")

    data_type = Prompt.ask("Data Type", default=clinical_data.data_type)
    value = Prompt.ask("Value", default=clinical_data.value)
    unit = Prompt.ask("Unit", default=clinical_data.unit)
    description = Prompt.ask("Description", default=clinical_data.description)

    update_clinical_data_use_case = make_update_clinical_data_use_case()
    clinical_data_updated = update_clinical_data_use_case.execute(patient_id, clinical_data.id, user.id, data_type, value, unit, description)

    if clinical_data_updated:
        console.io.print("\n[bold green]Clinical data updated successfully.[/bold green]")
        sleep(1)
        clear()
        return
    else:
        console.io.print("\n[bold red]Failed to update clinical datas.[/bold red]")
        sleep(3)
        clear()
        return