from typing import Optional

from core.entities.patient import Patient


class GetPatientByIdUseCase:
    def __init__(self, patient_repository):
        self.patient_repository = patient_repository

    def execute(self, patient_id: str) -> Optional[Patient]:
        """
        Retrieve an active patient by ID.
        """
        return self.patient_repository.get_by_id(patient_id)