from dataclasses import dataclass

from core.entities.clinical_data import ClinicalData
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class ListClinicalDataByPatientIdUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository

    def execute(self, patient_id: str) -> list[ClinicalData]:
        """
        Get all clinical data for a specific patient.
        """
        try:
            patient = self.patient_repository.get_by_id(patient_id)

            if not patient:
                console.io.print(f"\n[bold red]Patient with ID {patient_id} not found.[/bold red]")
                return []

            clinical_data = self.clinical_data_repository.list_by_patient_id(patient_id)

            return clinical_data
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get clinical data: {str(e)}[/bold red]")