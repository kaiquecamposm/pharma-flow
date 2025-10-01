from dataclasses import dataclass

from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository


@dataclass
class ArchivePatientUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository, audit_log_repository: AuditLogRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id, patient_id) -> bool:
        """
        Archive a patient.

        Time Complexity Analysis:

        - Archive patient:
            - O(1)

        - Check if patient has clinical data:
            - O(C), C = number of clinical data entries for this patient

        - Archive clinical data:
            - O(C), iterates over all clinical data for this patient

        - Audit log insertion:
            - O(1)

        Total Complexity:
            - O(P + C) in the worst case
            - Dominated by linear searches over patient list and clinical data list

        Best / Average / Worst Case:
            - Best: O(1) if patient is first in list and has no clinical data
            - Worst: O(P + C) if patient is last and has clinical data entries
        """
        try:
            is_patient_archived = self.patient_repository.inactivate(patient_id)

            if not is_patient_archived:
                raise ValueError("Patient not found")

            has_clinical_data = self.clinical_data_repository.list_by_patient_id(patient_id)

            if has_clinical_data:
                is_clinical_data_archived = self.clinical_data_repository.inactivate_by_patient_id(patient_id)

                if not is_clinical_data_archived:
                    raise ValueError("Failed to inactivate clinical data")

            self.audit_log_repository.add(
                user_id=user_id,
                action="ARCHIVE_PATIENT",
                target_id=patient_id,
                target_type="Patient, ClinicalData",
                details=f"Archived patient with ID: {patient_id}",
            )

            return is_patient_archived
        except Exception as e:
            raise ValueError(f"Failed to archive patient: {str(e)}")