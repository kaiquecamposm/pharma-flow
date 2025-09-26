from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_user_repository import (
    JSONUserRepository,
)
from core.use_cases.register_user import RegisterUserUseCase


# Factory to create an instance of RegisterUserUseCase
def make_register_user_use_case() -> RegisterUserUseCase:
    user_repository = JSONUserRepository()
    audit_log_repository = JSONAuditLogRepository()
    
    use_case = RegisterUserUseCase(user_repository, audit_log_repository)

    return use_case