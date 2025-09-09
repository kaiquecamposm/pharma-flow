from core.use_cases.factories import make_register_patient_use_case


def menu():
    print("1. Register Patient")
    print("2. Exit")
    return input("Choose an option: ")

def main():
    while True:
        choice = menu()
        if choice == "1":
            print("Registering patient...")

            patient_data = {
                "name": input("Enter patient name: "),
                "age": input("Enter patient age: "),
                "gender": input("Enter patient gender: ")
            }

            use_case = make_register_patient_use_case()

            print("Patient registered successfully.")
        elif choice == "2":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()