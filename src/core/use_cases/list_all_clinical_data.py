from dataclasses import dataclass

from core.entities.clinical_data import ClinicalData
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.clinical_data_repository import ClinicalDataRepository
from utils import console


@dataclass
class ListAllClinicalDataUseCase:
    def __init__(self, clinical_data_repository: ClinicalDataRepository, audit_log_repository: AuditLogRepository):
        self.clinical_data_repository = clinical_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id) -> list[ClinicalData]:
        """
        Get all clinical data.
        """
        try:
            clinical_data = self.clinical_data_repository.list_all()

            self.audit_log_repository.add({
                "user_id": user_id,
                "action": "LIST_CLINICAL_DATA",
                "target_id": "*MULTIPLE*",
                "target_type": "ClinicalData",
                "details": f"Listed {len(clinical_data)} clinical data entries."
            })

            return clinical_data
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get clinical data: {str(e)}[/bold red]")