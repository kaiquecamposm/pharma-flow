from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_clinical_data_repository import (
    JSONClinicalDataRepository,
)
from core.repositories.json.json_patient_repository import JSONPatientRepository
from core.use_cases.archive_patient import ArchivePatientUseCase


# Factory to create an instance of ArchivePatientUseCase
def make_archive_patient_use_case() -> ArchivePatientUseCase:
    patient_repository = JSONPatientRepository()
    clinical_data_repository = JSONClinicalDataRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = ArchivePatientUseCase(patient_repository, clinical_data_repository, audit_log_repository)

    return use_case