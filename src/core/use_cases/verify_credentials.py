from dataclasses import dataclass
from typing import Optional

from core.entities.user import User
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.user_repository import UserRepository
from utils import console


@dataclass
class VerifyCredentialsUseCase:
    def __init__(self, user_repository: UserRepository, audit_log_repository: AuditLogRepository):
        self.user_repository = user_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, email: str, password: str) -> Optional[User]:
        """
        Verify user credentials.
        Business rules:
        - Check if the email exists in the repository.
        """
        try:
            user = self.user_repository.get_by_email(email)

            if not user or user.password != password:
                return None
        
            self.audit_log_repository.add({
                "user_id": user.id,
                "action": "LOGIN",
                "target_id": user.id,
                "target_type": "User",
                "details": f"User {user.email} logged in."
            })

            return user

        except Exception as e:
            raise console.io.print_exception(f"Failed to verify credentials: {str(e)}")