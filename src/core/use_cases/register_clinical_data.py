from dataclasses import dataclass

from core.entities.clinical_data import ClinicalData
from core.repositories.clinical_data_repository import ClinicalDataRepository
from utils import console


@dataclass
class RegisterClinicalDataUseCase:
    def __init__(self, clinical_data_repository: ClinicalDataRepository):
        self.clinical_data_repository = clinical_data_repository

    def execute(self, clinical_data: ClinicalData) -> ClinicalData:
        """
        Register a new clinical data entry.
        Business rules:
        - Ensure the patient ID is valid (exists in the system).
        """
        try:
            new_clinical_data = ClinicalData(
                patient_id = clinical_data.patient_id,
                data_type = clinical_data.data_type,
                value = clinical_data.value,
                unit = clinical_data.unit,
                description = clinical_data.description,
                user_id = clinical_data.user_id
            )
            saved_clinical_data = self.clinical_data_repository.add(new_clinical_data)

            if saved_clinical_data is None:
                raise ValueError("\n[bold red]Failed to register clinical data.[/bold red]")

            return saved_clinical_data
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to register clinical data: {str(e)}[/bold red]")