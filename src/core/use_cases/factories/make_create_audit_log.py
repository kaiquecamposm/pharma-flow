from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.use_cases.create_register_audit_log import CreateAuditLogUseCase


# Factory to create an instance of CreateAuditLogUseCase
def make_create_audit_log_use_case() -> CreateAuditLogUseCase:
    audit_log_repository = JSONAuditLogRepository()

    use_case = CreateAuditLogUseCase(audit_log_repository)

    return use_case