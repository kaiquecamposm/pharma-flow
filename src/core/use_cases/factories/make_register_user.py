from core.repositories.json.json_user_repository import (
    JSONUserRepository,
)
from core.use_cases.register_user import RegisterUserUseCase


# Factory to create an instance of RegisterUserUseCase
def make_register_user_use_case() -> RegisterUserUseCase:
    user_repository = JSONUserRepository()
    
    use_case = RegisterUserUseCase(user_repository)

    return use_case