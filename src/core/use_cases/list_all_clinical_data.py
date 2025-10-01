from dataclasses import dataclass
from typing import List

from core.entities.clinical_data import ClinicalData
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.clinical_data_repository import ClinicalDataRepository


@dataclass
class ListAllClinicalDataUseCase:
    def __init__(self, clinical_data_repository: ClinicalDataRepository, audit_log_repository: AuditLogRepository):
        self.clinical_data_repository = clinical_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id) -> List[ClinicalData]:
        """
        Get all clinical data.

        Time Complexity Analysis:

        - List all clinical data:
            - O(n), n = total number of clinical data entries (linear traversal of list)

        - Audit log insertion:
            - O(1)

        Total Complexity:
        - O(n), dominated by the linear traversal of the clinical data list

        Best / Average / Worst Case:
        - Linear in the number of clinical data entries
        """
        try:
            clinical_data = self.clinical_data_repository.list_all()

            self.audit_log_repository.add(
                user_id=user_id,
                action="LIST_CLINICAL_DATA",
                target_id="*MULTIPLE*",
                target_type="ClinicalData",
                details=f"Listed {len(clinical_data)} clinical data entries."
            )

            return clinical_data
        except Exception as e:
            raise Exception(f"\nFailed to get clinical data: {str(e)}")