from core.commands import login_command, register_professional_command
from utils import show_menu


def main():
    is_authenticated = login_command.execute()

    if is_authenticated == "Admin":
        show_menu.execute("ADMIN MENU", {
            "1": ("Register Professional", register_professional_command.execute),
            "2": ("Exit", None)
        })
    else:
        show_menu.execute("USER MENU", {
            "1": ("Exit", None)
        })


if __name__ == "__main__":
    main()