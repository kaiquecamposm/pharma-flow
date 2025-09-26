from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_user_repository import (
    JSONUserRepository,
)
from core.use_cases.verify_credentials import VerifyCredentialsUseCase


# Factory to create an instance of VerifyCredentialsUseCase
def make_verify_credentials_use_case() -> VerifyCredentialsUseCase:
    user_repository = JSONUserRepository()
    audit_log_repository = JSONAuditLogRepository()
    
    use_case = VerifyCredentialsUseCase(user_repository, audit_log_repository)

    return use_case