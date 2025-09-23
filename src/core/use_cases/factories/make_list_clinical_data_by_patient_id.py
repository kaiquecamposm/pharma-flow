from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.repositories.json.json_patient_repository import JSONPatientRepository
from core.use_cases.list_clinical_data_by_patient_id import (
    ListClinicalDataByPatientIdUseCase,
)


# Factory to create an instance of ListClinicalDataByPatientIdUseCase
def make_list_clinical_data_by_patient_id_use_case() -> ListClinicalDataByPatientIdUseCase:
    patient_repository = JSONPatientRepository()
    clinical_data_repository = JSONClinicalDataRepository()

    use_case = ListClinicalDataByPatientIdUseCase(patient_repository, clinical_data_repository)

    return use_case