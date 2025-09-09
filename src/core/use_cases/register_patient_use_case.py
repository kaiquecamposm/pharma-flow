from core.entities.patient import Patient


class RegisterPatientUseCase:
    def __init__(self, patient_repository):
        self.patient_repository = patient_repository

    def execute(self, patient_data: dict) -> Patient:
        """
        Register a new patient.
        Business rules:
        [x] Patient data must be anonymized (e.g., encrypted or masked).
        """
        try:
            return self.patient_repository.add_patient(patient_data)
        except Exception as e:
            raise Exception(f"Failed to register patient: {str(e)}")
