from core.entities.patient import Patient
from core.repositories.patient_repository import PatientRepository


class UpdatePatientUseCase:
    def __init__(self, patient_repository: PatientRepository):
        self.patient_repository = patient_repository

    def execute(self, patient_data: Patient) -> Patient:
        """
        Update patient data without overwriting (increments version).
        """
        return self.patient_repository.update(patient_data)