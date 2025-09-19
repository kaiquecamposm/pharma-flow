from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.repositories.json.json_patient_repository import JSONPatientRepository
from core.use_cases.detected_outliers_in_clinical_data import (
    DetectedOutliersInClinicalDataUseCase,
)


# Factory to create an instance of DetectedOutliersInClinicalDataUseCase
def make_detected_outliers_in_clinical_data_use_case() -> DetectedOutliersInClinicalDataUseCase:
    patient_repository = JSONPatientRepository()
    clinical_data_repository = JSONClinicalDataRepository()

    use_case = DetectedOutliersInClinicalDataUseCase(patient_repository, clinical_data_repository)

    return use_case