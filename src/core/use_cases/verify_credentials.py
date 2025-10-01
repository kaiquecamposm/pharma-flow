from dataclasses import dataclass
from typing import Optional

from core.entities.user import User
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.user_repository import UserRepository


@dataclass
class VerifyCredentialsUseCase:
    def __init__(self, user_repository: UserRepository, audit_log_repository: AuditLogRepository):
        self.user_repository = user_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, email: str, password: str) -> Optional[User]:
        """
        Verify user credentials.

        Time Complexity Analysis:

        - Fetch user by email:
            - O(n), n = total number of users (linear search in list)

        - Password verification:
            - O(1) (simple comparison)

        - Audit log insertion:
            - O(1)

        Total Complexity:
        - O(n), dominated by the linear search for the user by email

        Best / Average / Worst Case:
        - Linear in the number of users
        """
        try:
            user = self.user_repository.get_by_email(email)

            if not user or user.password != password:
                return None
        
            self.audit_log_repository.add(
                user_id=user.id,
                action="LOGIN",
                target_id=user.id,
                target_type="User",
                details=f"User {user.email} logged in."
            )

            return user
        except Exception as e:
            raise Exception(f"Error verifying credentials: {e}")