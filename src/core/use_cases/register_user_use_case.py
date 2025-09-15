from dataclasses import dataclass

from core.entities.user import User
from core.repositories.user_repository import (
    UserRepository,
)
from utils import console


@dataclass
class RegisterUserUseCase:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    def execute(self, user_data: User) -> User:
        """
        Register a new user.
        Business rules:
        - Ensure the email is unique (not already registered).
        - Hash the password before storing (omitted here for simplicity).
        - Assign the appropriate role to the user.
        """
        try:
            is_exist_email = self.user_repository.get_by_email(user_data.email)

            if is_exist_email:
                raise ValueError("\n[bold red]Email already registered.[/bold red]")

            new_user = User(
                email=user_data.email,
                password=user_data.password,
                full_name=user_data.full_name,
                role_name=user_data.role_name,
                active=user_data.active,
            )

            saved_user = self.user_repository.add(new_user)

            if saved_user is None:
                raise ValueError("\n[bold red]Failed to register user.[/bold red]")

            return saved_user
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to register user: {str(e)}[/bold red]")