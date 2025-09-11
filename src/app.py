import base64
import re
import time

from core.entities.professional import Professional
from core.use_cases.factories.make_register_professional_use_case import (
    makeRegisterProfessionalUseCase,
)
from utils import clear_terminal


def register_professional():
    username = input("Username: ").strip()
    full_name = input("Full name: ").strip()
    email = input("Email: ").strip()

    # Verifica formato do email
    email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(email_regex, email):
        print("Invalid email format.")
        return

    # Seleção de cargos
    roles = ["Researcher", "Lab Technician", "Quality Auditor", "Environmental Officer", "Trainer", "Manager"]
    print("Select role:")
    for idx, role in enumerate(roles, 1):
        print(f"{idx}. {role}")
    role_choice = input("Enter the number for your role: ").strip()
    try:
        role_idx = int(role_choice) - 1
        if role_idx < 0 or role_idx >= len(roles):
            print("Invalid role selection.")
            return
        role_name = roles[role_idx]
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    active = input("Active (true/false): ").strip().lower() == "true"

    # Converte nome e email para base64
    full_name_b64 = base64.b64encode(full_name.encode("utf-8")).decode("utf-8")
    email_b64 = base64.b64encode(email.encode("utf-8")).decode("utf-8")

    professional = Professional(
        username=username,
        full_name=full_name_b64,
        email=email_b64,
        role_name=role_name,
        active=active
    )

    use_case = makeRegisterProfessionalUseCase()
    use_case.execute(professional)

    print("Professional registered successfully.")

def login():
    print("Login")
    username = input("Username: ")
    password = input("Password: ")
    
    if username == "admin" and password == "admin":
        print(f"Welcome, {username}!\n")
        time.sleep(1)
        clear_terminal.clear()
        return True
    else:
        print("Invalid credentials.")
        time.sleep(1)
        clear_terminal.clear()
        return False

def menu():
    print("\nMenu")
    print("1. Register Professional")
    print("2. Exit")

    choice = input("\nChoose an option: ")
    time.sleep(1)
    clear_terminal.clear()

    return choice

def main():
    is_admin = login()

    if not is_admin:
        print("Admin access required.")

    time.sleep(1)
    clear_terminal.clear()

    choice = menu()    

    while True:
        if choice == "1":
            register_professional()

            time.sleep(1)
            clear_terminal.clear()

            choice = menu()
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again .")

if __name__ == "__main__":
    main()