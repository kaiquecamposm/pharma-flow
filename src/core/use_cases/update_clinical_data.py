from dataclasses import dataclass
from typing import Optional

from core.entities.clinical_data import ClinicalData
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository
from utils import console


@dataclass
class UpdateClinicalDataUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository, audit_log_repository: AuditLogRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, patient_id, id, user_id, data_type, value, unit, description) -> Optional[ClinicalData]:
        try:
            patient = self.patient_repository.get_by_id(patient_id)

            if not patient:
                console.io.print(f"[bold red]Patient with ID {patient_id} not found.[/bold red]")
                return None

            updated_clinical_data = self.clinical_data_repository.update({
                "id": id,
                "patient_id": patient_id,
                "data_type": data_type,
                "value": value,
                "unit": unit,
                "description": description,
            })

            self.audit_log_repository.add({
                "user_id": user_id,
                "action": "UPDATE_CLINICAL_DATA",
                "target_id": patient_id,
                "target_type": "Patient, ClinicalData",
                "details": f"Updated clinical data for patient: {patient_id}",
            })

            return updated_clinical_data
        except Exception as e:
            raise console.io.print_exception(f"Failed to update clinical data: {str(e)}")