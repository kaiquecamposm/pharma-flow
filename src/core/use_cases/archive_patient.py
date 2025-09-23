from dataclasses import dataclass

from core.entities.patient import Patient
from core.repositories.clinical_data_repository import ClinicalDataRepository
from core.repositories.patient_repository import PatientRepository


@dataclass
class ArchivePatientUseCase:
    def __init__(self, patient_repository: PatientRepository, clinical_data_repository: ClinicalDataRepository):
        self.patient_repository = patient_repository
        self.clinical_data_repository = clinical_data_repository

    def execute(self, patient_id) -> Patient:
        """
        Archive a patient.
        """
        try:
            patient_archived = self.patient_repository.inactivate(patient_id)

            if not patient_archived:
                raise ValueError("Patient not found")

            clinical_data_archived = self.clinical_data_repository.inactivate_by_patient_id(patient_id)

            if not clinical_data_archived:
                raise ValueError("Failed to inactivate clinical data")

            return patient_archived
        except Exception as e:
            raise ValueError(f"Failed to archive patient: {str(e)}")