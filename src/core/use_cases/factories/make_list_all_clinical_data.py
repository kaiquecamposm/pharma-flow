from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.use_cases.list_all_clinical_data import ListAllClinicalDataUseCase


# Factory to create an instance of ListAllClinicalDataUseCase
def make_list_all_clinical_data_use_case() -> ListAllClinicalDataUseCase:
    clinical_data_repository = JSONClinicalDataRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = ListAllClinicalDataUseCase(clinical_data_repository, audit_log_repository)

    return use_case