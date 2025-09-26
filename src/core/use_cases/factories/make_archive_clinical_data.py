from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.use_cases.archive_clinical_data import ArchiveClinicalDataUseCase


# Factory to create an instance of ArchiveClinicalDataUseCase
def make_archive_clinical_data_use_case() -> ArchiveClinicalDataUseCase:
    clinical_data_repository = JSONClinicalDataRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = ArchiveClinicalDataUseCase(clinical_data_repository, audit_log_repository)

    return use_case