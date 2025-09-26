from utils import console


def select_lote(lotes_and_indicators: list):
    if not lotes_and_indicators:
        console.io.print("[bold red]No lotes found.[/bold red]")
        return None

    console.io.print("[bold cyan]Select a lote:[/bold cyan]\n")
    for idx, lote in enumerate(lotes_and_indicators, start=1):
        console.io.print(f"[bold white]{idx}.[/bold white] {lote['product_name']} ({lote['lote_id']}) - {lote['quantity']} | {lote['start_date']} to {lote['end_date']}")

    while True:
        try:
            choice = int(console.io.input("\nEnter the number of the lote: "))
            if 1 <= choice <= len(lotes_and_indicators):
                return lotes_and_indicators[choice - 1]["lote_id"]
            else:
                console.io.print("[bold red]Invalid choice. Please try again.[/bold red]")
        except ValueError:
            console.io.print("[bold red]Please enter a valid number.[/bold red]")