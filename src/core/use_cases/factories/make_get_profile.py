from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_user_repository import JSONUserRepository
from core.use_cases.get_profile import GetProfileUseCase


# Factory to create an instance of GetProfileUseCase
def make_get_profile_use_case() -> GetProfileUseCase:
    user_repository = JSONUserRepository()
    audit_log_repository = JSONAuditLogRepository()
    
    use_case = GetProfileUseCase(user_repository, audit_log_repository)

    return use_case