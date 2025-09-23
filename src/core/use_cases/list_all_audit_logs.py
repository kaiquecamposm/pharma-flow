from dataclasses import dataclass

from core.entities.audit_log import AuditLog
from core.repositories.audit_log_repository import AuditLogRepository
from utils import console


@dataclass
class ListAllAuditLogsUseCase:
    def __init__(self, audit_log_repository: AuditLogRepository):
        self.audit_log_repository = audit_log_repository

    def execute(self) -> list[AuditLog]:
        """
        Get all audit logs.
        """
        try:
            audit_logs = self.audit_log_repository.list_all()

            return audit_logs
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get audit logs: {str(e)}[/bold red]")