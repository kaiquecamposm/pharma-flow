from dataclasses import dataclass

from core.entities.patient import Patient
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class RegisterPatientUseCase:
    def __init__(self, patient_repository: PatientRepository):
        self.patient_repository = patient_repository

    def execute(self, patient_data: Patient) -> Patient:
        """
        Register a new patient.
        Business rules:
        - Ensure the email is unique (not already registered).
        """
        try:
            is_exist_email = self.patient_repository.get_by_email(patient_data.email)

            if is_exist_email:
                raise ValueError("\n[bold red]Email already registered.[/bold red]")

            new_patient = Patient(
                full_name=patient_data.full_name,
                email=patient_data.email,
                dob=patient_data.dob,
                gender=patient_data.gender,
                clinical_history=patient_data.clinical_history,
                active=patient_data.active,
            )
            
            saved_user = self.patient_repository.add(new_patient)

            if new_patient is None:
                raise ValueError("\n[bold red]Failed to register patient.[/bold red]")

            return saved_user
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to register patient: {str(e)}[/bold red]")