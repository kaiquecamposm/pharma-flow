class DeactivatePatientUseCase:
    def __init__(self, patient_repository):
        self.patient_repository = patient_repository

    def execute(self, patient_id: str) -> bool:
        """
        Deactivate a patient without physical deletion.
        """
        return self.patient_repository.inactivate(patient_id)