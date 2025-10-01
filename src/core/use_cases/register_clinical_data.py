from dataclasses import dataclass

from core.entities.clinical_data import ClinicalData
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.clinical_data_repository import ClinicalDataRepository


@dataclass
class RegisterClinicalDataUseCase:
    def __init__(self, clinical_data_repository: ClinicalDataRepository, audit_log_repository: AuditLogRepository):
        self.clinical_data_repository = clinical_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, data_type: str, value: str, unit: str, description: str, user_id: str, patient_id: str) -> ClinicalData:
        """
        Complexity Analysis:

        - Register Clinical Data: O(1) for adding a new clinical data entry.
        - Audit Logging: O(1) for adding a log entry.

        Overall Complexity: O(1)
        """
        try:
            saved_clinical_data = self.clinical_data_repository.add(data_type, value, unit, description, user_id, patient_id)

            if saved_clinical_data is None:
                raise ValueError("\n[bold red]Failed to register clinical data.[/bold red]")

            self.audit_log_repository.add(
                user_id=user_id,
                action="REGISTER_CLINICAL_DATA",
                target_id=user_id,
                target_type="ClinicalData",
                details=f"Registered clinical data for patient ID {patient_id}"
            )

            return saved_clinical_data
        except Exception as e:
            raise Exception(f"\nFailed to register clinical data: {str(e)}")