from time import sleep

from rich.prompt import Prompt

from core.entities.lote import Lote
from core.entities.production_data import ProductionData
from core.use_cases.factories import make_register_lote_use_case
from utils import console
from utils.clear_terminal import clear


def register_lote_command(user_id: str):
    console.io.print("[bold cyan]--- Register Lote ---[/bold cyan]\n")

    lote_data = Lote(
        code=Prompt.ask("[green]Lote Code[/green]").strip(),
        product_name=Prompt.ask("[green]Product Name[/green]").strip(),
        start_date=Prompt.ask("[green]Start Date (YYYY-MM-DD)[/green]").strip(),
        end_date=Prompt.ask("[green]End Date (YYYY-MM-DD)[/green]").strip(),
        user_id=user_id,
    )

    console.io.print("\n[bold green]Lote registered successfully.[/bold green]")
    sleep(1)
    clear()

    console.io.print("[bold cyan]--- Register Production Data ---[/bold cyan]\n")

    production_data = ProductionData(
        quantity=float(Prompt.ask("[green]Quantity Produced (units)[/green]").strip()),
        energy_consumption=float(Prompt.ask("[green]Energy Consumption (kWh)[/green]").strip()),
        emissions=float(Prompt.ask("[green]Emissions (kg CO2)[/green]").strip()),
        recovered_solvent_volume=float(Prompt.ask("[green]Recovered Solvent Volume (L)[/green]").strip()),
        user_id=user_id,
        lote_id=lote_data.id,
    )

    console.io.print("\n[bold green]Production Data registered successfully.[/bold green]")
    sleep(1)
    clear()

    register_lote_use_case = make_register_lote_use_case.execute()
    lote = register_lote_use_case.execute(lote_data, production_data)

    if lote:
        console.io.print("\n[bold green]Lote and production data registered successfully.[/bold green]")
        sleep(1)
        clear()
        return
    else:
        console.io.print("\n[bold red]Failed to register lote and production data.[/bold red]")
        sleep(2)
        clear()
        return