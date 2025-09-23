from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.use_cases.list_all_audit_logs import (
    ListAllAuditLogsUseCase,
)


# Factory to create an instance of ListAllAuditLogsUseCase
def make_list_all_audit_logs() -> ListAllAuditLogsUseCase:
    audit_log_repository = JSONAuditLogRepository()

    use_case = ListAllAuditLogsUseCase(audit_log_repository)

    return use_case