from rich.panel import Panel
from rich.prompt import Prompt

from utils import console
from utils.clear_terminal import clear


def show_menu(title: str, options: dict[str, callable]):
    """
    Show a menu with a given title and options.
        :param title: The title of the menu.
        :param options: A dictionary where keys are option labels and values are callables to execute.
        :return: None
    """
    console.io.print(Panel.fit(f"[bold cyan]{title.upper()}[/bold cyan]", border_style="bright_magenta"))

    # Display options
    for idx, label in enumerate(options.keys(), 1):
        console.io.print(f"[bold]{idx}.[/bold] {label}")

    choice = Prompt.ask("\n[bold]Choose an option[/bold]")
    clear()

    try:
        idx = int(choice) - 1
        label = list(options.keys())[idx]
        action = options[label]
        if action:
            action()
    except (ValueError, IndexError):
        raise ValueError("[bold red]Invalid option. Please try again.[/bold red]")
