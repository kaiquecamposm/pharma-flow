from time import sleep

from core.commands.users.login import login_command
from utils import console
from utils.clear_terminal import clear
from utils.menu import (
    analysis_menu,
    audit_menu,
    clinical_data_menu,
    education_menu,
    lotes_menu,
    patients_menu,
    users_menu,
)
from utils.show_menu import show_menu


def main():
    """
    Main loop of the system.
    
    Complexity Analysis:
    - While the user does not choose to exit:
        - Displaying the main menu → O(k), where k is the number of menu options
        - Calling the submenu → depends on the submenu function, T_submenu
    - Total approximate: O(1) per cycle + T_submenu
    - Since each submenu is usually O(m) → Total linear per interaction cycle
    """

    user = login_command()

    if not user:
        console.io.print("\n[bold red]Login failed. Exiting...[/bold red]")
        sleep(1)
        clear()
        return

    while True:
        main_options = {
            "Users": lambda: users_menu(user),
            "Patients": lambda: patients_menu(user),
            "Clinical Data": lambda: clinical_data_menu(user),
            "Lotes": lambda: lotes_menu(user),
            "Analysis": lambda: analysis_menu(user),
            "Education": lambda: education_menu(user),
            "Audit": lambda: audit_menu(user),
            "Exit": lambda: exit()
        }

        show_menu("🛠️  MENU", main_options)

if __name__ == "__main__":
    main()