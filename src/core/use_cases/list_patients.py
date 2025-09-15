from dataclasses import dataclass

from core.entities.patient import Patient
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class ListPatientsUseCase:
    def __init__(self, patient_repository: PatientRepository):
        self.patient_repository = patient_repository

    def execute(self) -> list[Patient]:
        """
        Get all patients.
        """
        try:
            patients = self.patient_repository.list_all()

            return patients
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get patients: {str(e)}[/bold red]")