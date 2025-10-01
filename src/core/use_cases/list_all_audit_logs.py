from dataclasses import dataclass

from core.entities.audit_log import AuditLog
from core.repositories.audit_log_repository import AuditLogRepository


@dataclass
class ListAllAuditLogsUseCase:
    def __init__(self, audit_log_repository: AuditLogRepository):
        self.audit_log_repository = audit_log_repository

    def execute(self) -> list[AuditLog]:
        """
        Get all audit logs.

        Time Complexity Analysis:

        - List all audit logs:
            - O(n), n = total number of audit log entries (linear traversal of list)

        Total Complexity:
        - O(n), dominated by the linear traversal of the audit log list

        Best / Average / Worst Case:
        - Linear in the number of audit log entries
        """
        try:
            audit_logs = self.audit_log_repository.list_all()

            return audit_logs
        except Exception as e:
            raise Exception(f"\nFailed to get audit logs: {str(e)}")