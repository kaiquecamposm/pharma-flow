

from time import sleep

from core.entities.audit_log import AuditLog
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_detected_outliers_in_clinical_data import (
    make_detected_outliers_in_clinical_data_use_case,
)
from utils import console
from utils.clear_terminal import clear


def detected_outliers_in_clinical_data_command(user_id: str):
    detected_outliers_in_clinical_data_use_case = make_detected_outliers_in_clinical_data_use_case()
    outliers = detected_outliers_in_clinical_data_use_case.execute()

    create_audit_log_use_case = make_create_audit_log_use_case()

    if outliers:
        console.io.print("[bold yellow]Detected Outliers in Clinical Data:[/bold yellow]\n")
        for patient_id, clinical_data in outliers.items():
            console.io.print(f"[cyan]Patient ID: {patient_id}[/cyan]")
            for data_type, stats in clinical_data.items():
                console.io.print(
                    f"  • {data_type} → Mean: {stats['mean']:.2f}, "
                    f"Std: {stats['std']:.2f}, "
                    f"Outliers: {stats['outliers']}"
                )
        
        create_audit_log_use_case.execute(AuditLog(
            user_id=user_id,
            action="DETECTED_OUTLIERS_IN_CLINICAL_DATA",
            target_id="*MULTIPLE*",
            target_type="Patient, ClinicalData",
            details=f"Detected outliers for {len(outliers)} patients."
        ))
    else:
        console.io.print("[bold green]No outliers detected in clinical data.[/bold green]")

    complete_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if complete_prompt:
        return