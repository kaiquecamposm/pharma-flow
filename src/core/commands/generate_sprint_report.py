

from time import sleep

from core.entities.audit_log import AuditLog
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_generate_sprint_report import (
    make_generate_sprint_report_use_case,
)
from utils import console
from utils.clear_terminal import clear


def generate_sprint_report_command(user_id: str):
    start_date = console.io.input(
        "[bold yellow]Enter the start date for the sprint report (YYYY-MM-DD): [/bold yellow]"
    )
    end_date = console.io.input(
        "[bold yellow]Enter the end date for the sprint report (YYYY-MM-DD): [/bold yellow]"
    )

    generate_sprint_report_use_case = make_generate_sprint_report_use_case()
    report = generate_sprint_report_use_case.execute(user_id, start_date, end_date)

    create_audit_log_use_case = make_create_audit_log_use_case()

    clear()

    if report:
        console.io.print("[bold yellow]Generated Sprint Report:[/bold yellow]\n")
        console.io.print("[bold underline]Regulatory Indicators:[/bold underline]")
        for key, value in report.regulatory_indicators.items():
            if value["status"] == "ALERT" or value["status"] == "OBESE":
                console.io.print(f"[bold]{key.replace('_', ' ').title()}:[/bold] [bold red]{value}[/bold red]")
            else:
                console.io.print(f"[bold]{key.replace('_', ' ').title()}:[/bold] [bold green]{value}[/bold green]")
            
        console.io.print("\n[bold underline]Environmental Indicators:[/bold underline]")
        for key, value in report.environmental_indicators.items():
            if value["status"] == "ALERT":
                console.io.print(f"[bold]{key.replace('_', ' ').title()}:[/bold] [bold red]{value}[/bold red]")
            else:
                console.io.print(f"[bold]{key.replace('_', ' ').title()}:[/bold] [bold green]{value}[/bold green]")

        create_audit_log_use_case.execute(AuditLog(
            user_id=user_id,
            action="GENERATE_SPRINT_REPORT",
            target_id="*MULTIPLE*",
            target_type="ProductionData, ClinicalData",
            details=f"Generated sprint report from {start_date} to {end_date}"
        ))
    else:
        console.io.print("[bold red]No data found for the given period.[/bold red]")

    complete_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if complete_prompt:
        return