from abc import ABC, abstractmethod

from core.entities.audit_log import AuditLog


class AuditLogRepository(ABC):
    """
    Interface for audit log repository.
    Defines methods for adding and retrieving audit logs.
    """
    @abstractmethod
    def add(self, audit_log: AuditLog) -> AuditLog:
        pass

    @abstractmethod
    def list_all(self) -> list[AuditLog]:
        pass