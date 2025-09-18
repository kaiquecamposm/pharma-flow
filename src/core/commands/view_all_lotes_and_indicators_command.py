from time import sleep

from core.use_cases.factories import (
    make_view_all_lotes_and_indicators_use_case,
)
from utils import console
from utils.clear_terminal import clear


def view_all_lotes_and_indicators_command():
    console.io.print("[bold cyan]--- View Lotes ---[/bold cyan]")

    view_all_lotes_and_indicators_use_case = make_view_all_lotes_and_indicators_use_case.execute()
    data = view_all_lotes_and_indicators_use_case.execute()

    if data:
        for idx, item in enumerate(data, start=1):
            if idx > 1:
                console.io.print("-" * 40)
            console.io.print(f"[bold]{idx}. Product: {item['product_name']} | Quantity: {item['quantity']} | Production Date: {item['end_date']} | Emissions (kg CO2): {item['ambient_indicators']['emissions']} | Energy Consumption (kWh): {item['ambient_indicators']['energy_consumption']} | Recovered Solvent Volume (L): {item['ambient_indicators']['recovered_solvent_volume']} | Registration Date: {item['registration_date']}")
    else:
        raise ValueError(console.io.print("\n[bold red]Failed to retrieve lotes data.[/bold red]"))

    continue_prompt = console.io.input("\n[bold yellow]Press Enter to return to the main menu...[/bold yellow]")
    sleep(1)
    clear()

    if continue_prompt:
        return