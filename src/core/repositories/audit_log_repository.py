from abc import ABC, abstractmethod

from core.entities.audit_log import AuditLog


class AuditLogRepository(ABC):
    """
    Interface for audit log repository.
    Defines methods for adding and retrieving audit logs.
    """
    @abstractmethod
    def add(self, user_id: str, action: str, target_id: str, target_type: str, details: str) -> AuditLog:
        pass

    @abstractmethod
    def list_all(self) -> list[AuditLog]:
        pass