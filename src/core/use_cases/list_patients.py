from dataclasses import dataclass
from typing import List

from core.entities.patient import Patient
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.patient_repository import PatientRepository


@dataclass
class ListPatientsUseCase:
    def __init__(self, patient_repository: PatientRepository, audit_log_repository: AuditLogRepository):
        self.patient_repository = patient_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id: str) -> List[Patient]:
        """
        Complexity Analysis:

        - List Patients: O(n) where n is the number of patients in the repository.
        - Audit Logging: O(1) for adding a log entry.

        Overall Complexity: O(n)
        """
        try:
            patients = self.patient_repository.list_all()

            self.audit_log_repository.add(
                user_id=user_id,
                action="LIST_PATIENTS",
                target_id="*MULTIPLE*",
                target_type="Patient",
                details=f"Listed {len(patients)} patients."
            )

            return patients
        except Exception as e:
            raise Exception(f"\nFailed to get patients: {str(e)}")