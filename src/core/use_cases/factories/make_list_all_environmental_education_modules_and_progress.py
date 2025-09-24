from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_education_module_repository import (
    JSONEducationModuleRepository,
)
from core.repositories.json.json_education_progress_repository import (
    JSONEducationProgressRepository,
)
from core.use_cases.list_all_environmental_education_modules_and_progress import (
    ListAllEnvironmentalEducationModulesAndProgressUseCase,
)


# Factory to create an instance of AccessEnvironmentalEducationModulesUseCase
def make_list_all_environmental_education_modules_and_progress_use_case() -> ListAllEnvironmentalEducationModulesAndProgressUseCase:
    education_module_repository = JSONEducationModuleRepository()
    education_progress_repository = JSONEducationProgressRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = ListAllEnvironmentalEducationModulesAndProgressUseCase(
        education_module_repository,
        education_progress_repository,
        audit_log_repository
    )

    return use_case