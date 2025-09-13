from dataclasses import dataclass
from typing import Optional

from core.entities.user import User
from core.repositories.user_repository import UserRepository
from utils import console


@dataclass
class VerifyCredentialsUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, email: str, password: str) -> Optional[User]:
        """
        Verify user credentials.
        Business rules:
        - Check if the email exists in the repository.
        """
        try:
            user = self.user_repository.get_by_email(email)

            if user and user.password == password:
                return user
            return None

        except Exception as e:
            raise console.io.print_exception(f"Failed to verify credentials: {str(e)}")