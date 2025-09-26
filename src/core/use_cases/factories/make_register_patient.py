from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_patient_repository import JSONPatientRepository
from core.use_cases.register_patient import RegisterPatientUseCase


# Factory to create an instance of RegisterPatientUseCase
def make_register_patient_use_case() -> RegisterPatientUseCase:
    patient_repository = JSONPatientRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = RegisterPatientUseCase(patient_repository, audit_log_repository)

    return use_case