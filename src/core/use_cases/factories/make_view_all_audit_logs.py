from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.use_cases.view_all_audit_logs import ViewAllAuditLogsUseCase


# Factory to create an instance of ViewAllAuditLogsUseCase
def make_view_all_audit_logs() -> ViewAllAuditLogsUseCase:
    audit_log_repository = JSONAuditLogRepository()

    use_case = ViewAllAuditLogsUseCase(audit_log_repository)

    return use_case