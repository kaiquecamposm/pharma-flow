from dataclasses import dataclass

from core.entities.user import User
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.user_repository import (
    UserRepository,
)


@dataclass
class RegisterUserUseCase:
    def __init__(self, user_repository: UserRepository, audit_log_repository: AuditLogRepository):
        self.user_repository = user_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id: str, email: str, password: str, full_name: str, role_name: str, active: bool) -> User:
        """
        Registers a new user in the system.

        Time Complexity Analysis:

        - Check if email exists:
            - O(n), n = total number of users (linear search in list)

        - Add user:
            - O(1) (append to the end of the list)

        - Audit log insertion:
            - O(1)

        Total Complexity:
        - O(n), dominated by the linear search for email

        Best / Average / Worst Case:
        - Linear in the number of users in the repository
        """
        try:
            is_same_email = self.user_repository.get_by_email(email)

            if is_same_email:
                raise ValueError("\n[bold red]Email already registered.[/bold red]")

            saved_user = self.user_repository.add(email, password, full_name, role_name, active)

            if saved_user is None:
                raise ValueError("\n[bold red]Failed to register user.[/bold red]")

            self.audit_log_repository.add(
                user_id=user_id,
                action="REGISTER_USER",
                target_id=saved_user.id,
                target_type="User",
                details=f"User {full_name} registered with role {role_name}."
            )

            return saved_user
        except Exception as e:
            raise Exception(f"\nFailed to register user: {str(e)}")