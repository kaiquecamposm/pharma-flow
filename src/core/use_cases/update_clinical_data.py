from dataclasses import dataclass
from typing import Optional

from core.entities.clinical_data import ClinicalData
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository


@dataclass
class  UpdateClinicalDataUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository, audit_log_repository: AuditLogRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, patient_id, id, user_id, data_type, value, unit, description) -> Optional[ClinicalData]:
        """
        Updates a clinical data entry for a specific patient.

        Time Complexity Analysis:

        - Fetch patient by ID:
            - O(n), n = total number of patients (linear search in list)

        - Update clinical data:
            - O(m), m = total number of clinical data entries (linear search to find the entry in list)

        - Audit log insertion:
            - O(1)

        Total Complexity:
        - O(n + m), dominated by the linear searches in the patient and clinical data lists

        Best / Average / Worst Case:
        - Linear in the number of patients and clinical data entries
        """
        try:
            patient = self.patient_repository.get_by_id(patient_id)

            if not patient:
                raise ValueError(f"[bold red]Patient with ID {patient_id} not found.[/bold red]")

            updated_clinical_data = self.clinical_data_repository.update(id, user_id, data_type, value, unit, description)

            if not updated_clinical_data:
                raise ValueError(f"Clinical data with ID {id} not found or could not be updated.")

            self.audit_log_repository.add(
                user_id=user_id,
                action="UPDATE_CLINICAL_DATA",
                target_id=patient_id,
                target_type="Patient, ClinicalData",
                details=f"Updated clinical data for patient: {patient_id}",
            )

            return updated_clinical_data
        except Exception as e:
            raise Exception(f"Failed to update clinical data: {str(e)}")