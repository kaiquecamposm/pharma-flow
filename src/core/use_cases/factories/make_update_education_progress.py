from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_education_progress_repository import (
    JSONEducationProgressRepository,
)
from core.use_cases.update_education_progress import UpdateEducationProgressUseCase


# Factory to create an instance of UpdateEducationProgressUseCase
def make_update_education_progression_use_case() -> UpdateEducationProgressUseCase:
    education_progress_repository = JSONEducationProgressRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = UpdateEducationProgressUseCase(education_progress_repository, audit_log_repository)

    return use_case