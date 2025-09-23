from dataclasses import dataclass

from core.entities.clinical_data import ClinicalData
from core.repositories.clinical_data_repository import ClinicalDataRepository


@dataclass
class ArchiveClinicalDataUseCase:
    def __init__(self, clinical_data_repository: ClinicalDataRepository):
        self.clinical_data_repository = clinical_data_repository

    def execute(self, clinical_data_id) -> ClinicalData:
        """
        Archive a clinical data entry.
        """
        try:
            clinical_data_archived = self.clinical_data_repository.inactivate(clinical_data_id)

            if not clinical_data_archived:
                raise ValueError("Failed to inactivate clinical data")

            return clinical_data_archived
        except Exception as e:
            raise ValueError(f"Failed to archive clinical data: {str(e)}")