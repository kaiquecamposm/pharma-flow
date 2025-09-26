from time import sleep

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_archive_patient import make_archive_patient_use_case
from core.use_cases.factories.make_list_patients import make_list_patients_use_case
from utils import console
from utils.clear_terminal import clear
from utils.select_patient import select_patient


@authorize("patients")
def archive_patient_command(user: User):
    console.io.print("[bold cyan]--- Archive Patient ---[/bold cyan]\n")

    list_patients_use_case = make_list_patients_use_case()
    patients = list_patients_use_case.execute(user.id)

    patient_id = select_patient(patients)

    archive_patient_use_case = make_archive_patient_use_case()
    archived_patient = archive_patient_use_case.execute(user.id, patient_id)

    if not archived_patient:
        console.io.print(f"[bold red]Failed to archive patient with ID: {patient_id}[/bold red]")
        return

    console.io.print(f"\n[bold green]Patient with ID: {patient_id} archived successfully![/bold green]")
    sleep(2)
    clear()