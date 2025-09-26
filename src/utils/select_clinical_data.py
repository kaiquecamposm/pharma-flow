from core.entities.clinical_data import ClinicalData
from utils import console


def select_clinical_data(clinical_data: list[ClinicalData]):
    if not clinical_data:
        console.io.print("[bold red]No clinical data found.[/bold red]")
        return None

    console.io.print("[bold cyan]Select a clinical data:[/bold cyan]\n")
    for idx, data in enumerate(clinical_data, start=1):
        console.io.print(f"[bold white]{idx}.[/bold white] {data.id} - {data.data_type} ({data.value} {data.unit}) | {data.description}")

    while True:
        try:
            choice = int(console.io.input("\nEnter the number of the clinical data: "))
            if 1 <= choice <= len(clinical_data):
                return clinical_data[choice - 1].id
            else:
                console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
        except ValueError:
            console.io.print("[bold red]Please enter a valid number.[/bold red]")