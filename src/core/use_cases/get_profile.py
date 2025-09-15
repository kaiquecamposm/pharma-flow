from dataclasses import dataclass

from core.entities.user import User
from core.repositories.user_repository import UserRepository
from utils import console


@dataclass
class GetProfileUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_id: str) -> User:
        """
        Get user profile by ID.
        """
        try:
            profile = self.user_repository.get_by_id(user_id)
            
            if profile is None:
                raise ValueError("\n[bold red]User not found.[/bold red]")

            return profile
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get user profile: {str(e)}[/bold red]")