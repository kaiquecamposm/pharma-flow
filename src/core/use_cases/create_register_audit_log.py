from dataclasses import dataclass

from core.entities.audit_log import AuditLog
from core.repositories.audit_log_repository import AuditLogRepository


@dataclass
class CreateAuditLogUseCase:
    def __init__(self, audit_log_repository: AuditLogRepository):
        self.audit_log_repository = audit_log_repository

    def execute(self, audit_log: AuditLog) -> AuditLog:
        """
        Create a new audit log entry.
        """
        try:
            new_log = AuditLog(
                user_id=audit_log.user_id,
                action=audit_log.action,
                target_id=audit_log.target_id,
                target_type=audit_log.target_type,
                details=audit_log.details,
            )

            self.audit_log_repository.add(new_log)

            return new_log
        except Exception as e:
            raise ValueError(f"Failed to create audit log: {str(e)}")