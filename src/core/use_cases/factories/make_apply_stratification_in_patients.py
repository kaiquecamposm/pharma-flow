from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.repositories.json.json_patient_repository import JSONPatientRepository
from core.use_cases.apply_stratification_in_patients import (
    ApplyStratificationInPatientsUseCase,
)


# Factory to create an instance of ApplyStratificationInPatientsUseCase
def make_apply_stratification_in_patients_use_case() -> ApplyStratificationInPatientsUseCase:
    patient_repository = JSONPatientRepository()
    clinical_data_repository = JSONClinicalDataRepository()

    use_case = ApplyStratificationInPatientsUseCase(patient_repository, clinical_data_repository)

    return use_case