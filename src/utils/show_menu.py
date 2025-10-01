from collections import deque
from time import sleep

from rich.panel import Panel
from rich.prompt import Prompt

from utils import console
from utils.clear_terminal import clear

menu_stack = deque()


def show_menu(title: str, options: dict[str, callable]):
    """
    Show a menu with a Stack for history.
    
    Complexity Analysis:
    - Main loop iterating menu options → O(m), m = number of options
    - Access to dict options → O(1)
    - Stack operations (append/pop) → O(1)
    - Each action execution → depends on the called function, T_action
    - Total per menu call: O(m + T_action)

    Note: Loop eliminates recursion, ensuring predictable complexity
    """
    console.io.print(Panel.fit(f"[bold cyan]{title.upper()}[/bold cyan]", border_style="bright_magenta"))

    # Display options
    for idx, label in enumerate(options.keys(), 1):
        console.io.print(f"[bold]{idx}.[/bold] {label}")

    console.io.print(f"[bold]{len(options) + 1}.[/bold] Back")

    choice = Prompt.ask("\n[bold]Choose an option[/bold]")
    clear()

    try:
        idx = int(choice) - 1
        if idx == len(options):
            # Go back to the previous menu
            if menu_stack:
                prev_menu = menu_stack.pop()
                prev_menu()
            return

        label = list(options.keys())[idx]
        action = options[label]

        if action:
            menu_stack.append(lambda: show_menu(title, options))
            action()
            return # Return after action to avoid re-displaying the menu
    except (ValueError, IndexError):
        console.io.print("[bold red]Invalid option. Please try again.[/bold red]")
        sleep(1)
        clear()
