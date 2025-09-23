from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.repositories.json.json_patient_repository import JSONPatientRepository
from core.use_cases.update_clinical_data import UpdateClinicalDataUseCase


# Factory to create an instance of UpdateClinicalDataUseCase
def make_update_clinical_data_use_case() -> UpdateClinicalDataUseCase:
    patient_repository = JSONPatientRepository()
    clinical_data_repository = JSONClinicalDataRepository()

    use_case = UpdateClinicalDataUseCase(patient_repository, clinical_data_repository)

    return use_case