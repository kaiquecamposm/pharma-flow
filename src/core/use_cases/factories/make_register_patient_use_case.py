from src.core.repositories.patient_repository import PatientRepository
from src.core.use_cases.register_patient_use_case import RegisterPatientUseCase


def make_register_patient_use_case():
    patient_repository = PatientRepository()
    use_case = RegisterPatientUseCase(patient_repository)

    return use_case