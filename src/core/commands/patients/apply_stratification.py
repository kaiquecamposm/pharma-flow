from time import sleep

from core.entities.audit_log import AuditLog
from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_apply_stratification_in_patients import (
    make_apply_stratification_in_patients_use_case,
)
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from utils import console
from utils.clear_terminal import clear


@authorize("patients")
def apply_stratification_in_patients_command(user: User):
    console.io.print("[bold cyan]--- Stratification in Patients ---[/bold cyan]\n")

    apply_stratification_in_patients_use_case = make_apply_stratification_in_patients_use_case()
    stratification_patients = apply_stratification_in_patients_use_case.execute()

    if stratification_patients:
        for stratification in stratification_patients:
            priority = "[bold red]high[/bold red]" if stratification['priority'] == 1 else "[bold yellow]medium[/bold yellow]" if stratification['priority'] == 2 else "[bold green]low[/bold green]"

            console.io.print(f"[bold white]Patient:[/bold white] {stratification['patient_id']} | [bold white]Data type:[/bold white] {stratification['clinical_data']['data_type']} | [bold white]Value:[/bold white] {stratification['clinical_data']['value']} {stratification['clinical_data']['unit']} | [bold white]Priority:[/bold white] {priority}")

        create_audit_log_use_case = make_create_audit_log_use_case()
        create_audit_log_use_case.execute(AuditLog(
            user_id=user.id,
            action="APPLY_STRATIFICATION_IN_PATIENTS",
            target_id="*MULTIPLE*",
            target_type="Patient, ClinicalData",
            details=f"Apply stratification in {len(stratification_patients)} patients"
        ))
    else:
        console.io.print("[bold red]No stratification found.[/bold red]")

    continue_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if continue_prompt:
        return