from dataclasses import dataclass

from core.entities.clinical_data import ClinicalData
from core.repositories.clinical_data_repository import ClinicalDataRepository
from utils import console


@dataclass
class ViewClinicalDataUseCase:
    def __init__(self, clinical_data_repository: ClinicalDataRepository):
        self.clinical_data_repository = clinical_data_repository

    def execute(self) -> list[ClinicalData]:
        """
        Get all clinical data.
        """
        try:
            clinical_data = self.clinical_data_repository.list_all()

            return clinical_data
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get clinical data: {str(e)}[/bold red]")