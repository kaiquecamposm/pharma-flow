from dataclasses import dataclass

from core.entities.clinical_data import ClinicalData
from core.repositories.clinical_data_repository import ClinicalDataRepository


@dataclass
class ArchiveClinicalDataUseCase:
    def __init__(self, clinical_data_repository: ClinicalDataRepository, audit_log_repository: ClinicalDataRepository):
        self.clinical_data_repository = clinical_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id, clinical_data_id) -> ClinicalData:
        """
        Archive a clinical data entry.

        Time Complexity Analysis:

        - Archive clinical data:
            - O(N)
            (N = number of clinical data entries; assumes linear search in a list)

        - Audit log insertion:
            - O(1)

        Total Complexity:
            - O(N) in the worst case
            - Dominated by the linear scan over the clinical data list

        Best / Average / Worst Case:
            - Best: O(1) if the entry is first in the list
            - Worst: O(N) if the entry is last in the list
        """
        try:
            clinical_data_archived = self.clinical_data_repository.inactivate(clinical_data_id)

            if not clinical_data_archived:
                raise ValueError("Failed to inactivate clinical data")

            self.audit_log_repository.add(
                user_id=user_id,
                action="ARCHIVE_CLINICAL_DATA",
                target_id=clinical_data_id,
                target_type="ClinicalData",
                details=f"Archived clinical data with ID: {clinical_data_id}",
            )

            return clinical_data_archived
        except Exception as e:
            raise ValueError(f"Failed to archive clinical data: {str(e)}")