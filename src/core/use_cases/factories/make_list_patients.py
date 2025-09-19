from core.repositories.json.json_patient_repository import JSONPatientRepository
from core.use_cases.list_patients import ListPatientsUseCase


# Factory to create an instance of ListPatientsUseCase
def make_list_patients_use_case() -> ListPatientsUseCase:
    patient_repository = JSONPatientRepository()
    
    use_case = ListPatientsUseCase(patient_repository)

    return use_case