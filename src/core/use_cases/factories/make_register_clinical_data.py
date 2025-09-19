from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.use_cases.register_clinical_data import RegisterClinicalDataUseCase


# Factory to create an instance of RegisterClinicalDataUseCase
def make_register_clinical_data_use_case() -> RegisterClinicalDataUseCase:
    clinical_data_repository = JSONClinicalDataRepository()
    
    use_case = RegisterClinicalDataUseCase(clinical_data_repository)

    return use_case