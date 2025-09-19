from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.use_cases.view_all_clinical_data import ViewAllClinicalDataUseCase


# Factory to create an instance of ViewAllClinicalDataUseCase
def make_view_all_clinical_data_use_case() -> ViewAllClinicalDataUseCase:
    clinical_data_repository = JSONClinicalDataRepository()
    
    use_case = ViewAllClinicalDataUseCase(clinical_data_repository)

    return use_case