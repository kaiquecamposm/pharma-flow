

from time import sleep

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_generate_sprint_report import (
    make_generate_sprint_report_use_case,
)
from utils import console
from utils.clear_terminal import clear


@authorize("analysis")
def generate_sprint_report_command(user: User):
    start_date = console.io.input(
        "[bold yellow]Enter the start date for the sprint report (YYYY-MM-DD): [/bold yellow]"
    )
    end_date = console.io.input(
        "[bold yellow]Enter the end date for the sprint report (YYYY-MM-DD): [/bold yellow]"
    )

    generate_sprint_report_use_case = make_generate_sprint_report_use_case()
    report = generate_sprint_report_use_case.execute(user.id, start_date, end_date)

    clear()

    if not report:
        console.io.print("[bold red]No data found for the given period.[/bold red]")
        sleep(1)
        clear()
        return
    
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

    complete_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if complete_prompt:
        return