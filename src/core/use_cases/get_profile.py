from dataclasses import dataclass

from core.entities.user import User
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.user_repository import UserRepository


@dataclass
class GetProfileUseCase:
    def __init__(self, user_repository: UserRepository, audit_log_repository: AuditLogRepository):
        self.user_repository = user_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id: str) -> User:
        """
        Get user profile by ID.

        Time Complexity Analysis:

        - Fetch user by ID:
            - O(n), n = total number of users (linear search in list)

        - Audit log insertion:
            - O(1)

        Total Complexity:
        - O(n), dominated by the linear search for the user by ID

        Best / Average / Worst Case:
        - Linear in the number of users
        """
        try:
            profile = self.user_repository.get_by_id(user_id)
            
            if profile is None:
                raise ValueError("\n[bold red]User not found.[/bold red]")

            self.audit_log_repository.add(
                user_id=user_id,
                action="VIEW_PROFILE",
                target_id=user_id,
                target_type="User",
                details=f"User {profile.full_name} viewed their profile."
            )

            return profile
        except Exception as e:
            raise Exception(f"\nFailed to get user profile: {str(e)}")