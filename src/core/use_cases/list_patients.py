from dataclasses import dataclass

from core.entities.patient import Patient
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class ListPatientsUseCase:
    def __init__(self, patient_repository: PatientRepository, audit_log_repository: AuditLogRepository):
        self.patient_repository = patient_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id: str) -> list[Patient]:
        """
        Get all patients.
        """
        try:
            patients = self.patient_repository.list_all()

            self.audit_log_repository.add({
                "user_id": user_id,
                "action": "LIST_PATIENTS",
                "target_id": "*MULTIPLE*",
                "target_type": "Patient",
                "details": f"Listed {len(patients)} patients."
            })

            return patients
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get patients: {str(e)}[/bold red]")