from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.use_cases.view_clinical_data import ViewClinicalDataUseCase


# Factory to create an instance of ViewClinicalDataUseCase
def execute() -> ViewClinicalDataUseCase:
    clinical_data_repository = JSONClinicalDataRepository()
    
    use_case = ViewClinicalDataUseCase(clinical_data_repository)

    return use_case