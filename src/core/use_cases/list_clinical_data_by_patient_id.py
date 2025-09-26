from dataclasses import dataclass

from core.entities.clinical_data import ClinicalData
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class ListClinicalDataByPatientIdUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository, audit_log_repository: AuditLogRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id: str, patient_id: str) -> list[ClinicalData]:
        """
        Get all clinical data for a specific patient.
        """
        try:
            patient = self.patient_repository.get_by_id(patient_id)

            if not patient:
                console.io.print(f"\n[bold red]Patient with ID {patient_id} not found.[/bold red]")
                return []

            clinical_data = self.clinical_data_repository.list_by_patient_id(patient_id)

            self.audit_log_repository.add({
                "user_id": user_id,
                "action": "LIST_CLINICAL_DATA_BY_PATIENT_ID",
                "target_id": patient_id,
                "target_type": "Patient, ClinicalData",
                "details": f"Listed {len(clinical_data)} clinical data entries for patient ID {patient_id}",
            })

            return clinical_data
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get clinical data: {str(e)}[/bold red]")