from time import sleep

from core.entities.audit_log import AuditLog
from core.use_cases.factories.make_create_audit_log import (
    make_create_audit_log_use_case,
)
from core.use_cases.factories.make_view_all_lotes_and_indicators import (
    make_view_all_lotes_and_indicators_use_case,
)
from utils import console
from utils.clear_terminal import clear


def view_all_lotes_and_indicators_command(user_id: str):
    console.io.print("[bold cyan]--- View Lotes ---[/bold cyan]\n")

    view_all_lotes_and_indicators_use_case = make_view_all_lotes_and_indicators_use_case()
    lotes = view_all_lotes_and_indicators_use_case.execute()

    create_audit_log_use_case = make_create_audit_log_use_case()

    create_audit_log_use_case.execute(AuditLog(
        user_id=user_id,
        action="VIEW_ALL_LOTES_AND_INDICATORS",
        target_id="*MULTIPLE*",
        target_type="Lote, ProductionData",
        details="User viewed all lotes and their environmental indicators."
    ))

    if lotes:
        for idx, item in enumerate(lotes, start=1):
            if idx > 1:
                console.io.print("-" * 40)
            console.io.print(f"[bold]{idx}. Product: {item['product_name']} | Quantity: {item['quantity']} | Production Date: {item['end_date']} | Emissions (kg CO2): {item['ambient_indicators']['emissions']} | Energy Consumption (kWh): {item['ambient_indicators']['energy_consumption']} | Recovered Solvent Volume (L): {item['ambient_indicators']['recovered_solvent_volume']} | Registration Date: {item['registration_date']}")
    else:
        raise ValueError(console.io.print("[bold red]Failed to retrieve lotes data.[/bold red]"))

    continue_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if continue_prompt:
        return