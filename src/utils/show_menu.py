import time

from rich.panel import Panel
from rich.prompt import Prompt

from utils import console


def execute(title: str, options: dict[str, callable]):
    """
    Show a menu with given options and execute selected action.

    Args:
        title (str): Title of the menu.
        options (dict): Dict of options { "{key}": (description, function) }.
    """
    while True:
        console.io.print(Panel.fit(f"[bold cyan]🛠️  {title}[/bold cyan]", border_style="bright_magenta"))

        # Show options
        for key, (desc, _) in options.items():
            console.io.print(f"[bold green]{key}. {desc}[/bold green]")

        choice = Prompt.ask("\n[bold]Choose an option[/bold]")
        console.io.clear()

        if choice in options:
            desc, action = options[choice]

            # Execute function
            if action:
                action()

            if desc.lower() == "exit":
                console.io.print("[bold green]Exiting...[/bold green]")
                time.sleep(1)
                console.io.clear()
                return
        else:
            console.io.print("[bold red]Invalid option. Please try again.[/bold red]")
            time.sleep(2)
            console.io.clear()