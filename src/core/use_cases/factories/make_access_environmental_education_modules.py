from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_education_module_repository import (
    JSONEducationModuleRepository,
)
from core.repositories.json.json_education_progress_repository import (
    JSONEducationProgressRepository,
)
from core.use_cases.access_environmental_education_modules import (
    AccessEnvironmentalEducationModulesUseCase,
)


# Factory to create an instance of AccessEnvironmentalEducationModulesUseCase
def make_access_environmental_education_modules_use_case() -> AccessEnvironmentalEducationModulesUseCase:
    education_module_repository = JSONEducationModuleRepository()
    education_progress_repository = JSONEducationProgressRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = AccessEnvironmentalEducationModulesUseCase(
        education_module_repository,
        education_progress_repository,
        audit_log_repository
    )

    return use_case