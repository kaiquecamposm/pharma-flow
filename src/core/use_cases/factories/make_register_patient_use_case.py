from core.repositories.json.json_patient_repository import JSONPatientRepository
from core.use_cases.register_patient import RegisterPatientUseCase


# Factory to create an instance of RegisterPatientUseCase
def execute() -> RegisterPatientUseCase:
    user_repository = JSONPatientRepository()
    
    use_case = RegisterPatientUseCase(user_repository)

    return use_case