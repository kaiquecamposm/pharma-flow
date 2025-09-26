from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.use_cases.register_clinical_data import RegisterClinicalDataUseCase


# Factory to create an instance of RegisterClinicalDataUseCase
def make_register_clinical_data_use_case() -> RegisterClinicalDataUseCase:
    clinical_data_repository = JSONClinicalDataRepository()
    audit_log_repository = JSONAuditLogRepository()
    
    use_case = RegisterClinicalDataUseCase(clinical_data_repository, audit_log_repository)

    return use_case