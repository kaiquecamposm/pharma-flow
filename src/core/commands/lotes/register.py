from time import sleep

from rich.prompt import Prompt

from core.entities.user import User
from core.middlewares.authorize import authorize
from core.use_cases.factories.make_register_lote import make_register_lote_use_case
from utils import console
from utils.clear_terminal import clear


@authorize("lotes")
def register_lote_command(user: User):
    console.io.print("[bold cyan]--- Register Lote ---[/bold cyan]\n")

    code = Prompt.ask("[green]Lote Code[/green]").strip()
    product_name = Prompt.ask("[green]Product Name[/green]").strip()
    start_date = Prompt.ask("[green]Start Date (YYYY-MM-DD)[/green]").strip()
    end_date = Prompt.ask("[green]End Date (YYYY-MM-DD)[/green]").strip()

    console.io.print("\n[bold cyan]--- Register Production Data ---[/bold cyan]\n")

    quantity = float(Prompt.ask("[green]Quantity Produced (units)[/green]").strip())
    energy_consumption = float(Prompt.ask("[green]Energy Consumption (kWh)[/green]").strip())
    emissions = float(Prompt.ask("[green]Emissions (kg CO2)[/green]").strip())
    recovered_solvent_volume = float(Prompt.ask("[green]Recovered Solvent Volume (L)[/green]").strip())

    register_lote_use_case = make_register_lote_use_case()
    lote = register_lote_use_case.execute(code, product_name, start_date, end_date, quantity, energy_consumption, emissions, recovered_solvent_volume, user.id)

    if not lote:
        console.io.print("\n[bold red]Failed to register lote and production data.[/bold red]")
        sleep(1)
        clear()
        return
    
    console.io.print("\n[bold green]Lote and production data registered successfully.[/bold green]")
    sleep(1)
    clear()
    return