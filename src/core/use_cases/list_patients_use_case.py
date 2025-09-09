from typing import List

from core.entities.patient import Patient


class ListPatientUseCase:
    def __init__(self, patient_repository):
        self.patient_repository = patient_repository

    def execute(self) -> List[Patient]:
        """
        List all active patients.
        """
        return self.repository.list()