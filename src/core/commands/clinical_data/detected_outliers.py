

from time import sleep

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_detected_outliers_in_clinical_data import (
    make_detected_outliers_in_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear


@authorize("clinical_data")
def detected_outliers_in_clinical_data_command(user: User):
    detected_outliers_in_clinical_data_use_case = make_detected_outliers_in_clinical_data_use_case()
    outliers = detected_outliers_in_clinical_data_use_case.execute(user.id)

    if not outliers:
        console.io.print("[bold green]No outliers detected in production data.[/bold green]")
        sleep(1)
        clear()
        return

    console.io.print("[bold yellow]Detected Outliers in Clinical Data:[/bold yellow]\n")
    for patient_id, clinical_data in outliers.items():
        console.io.print(f"[cyan]Patient ID: {patient_id}[/cyan]")
        for data_type, stats in clinical_data.items():
            console.io.print(
                f"  • {data_type} → Mean: {stats['mean']:.2f}, "
                f"Std: {stats['std']:.2f}, "
                f"Outliers: {stats['outliers']}"
            )

    complete_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if complete_prompt:
        return