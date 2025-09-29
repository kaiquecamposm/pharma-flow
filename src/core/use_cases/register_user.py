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
        Register a new user.
        Business rules:
        - Ensure the email is unique (not already registered).
        - Hash the password before storing (omitted here for simplicity).
        - Assign the appropriate role to the user.
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