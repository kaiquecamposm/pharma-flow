from core.repositories.json.json_role_repository import JSONRoleRepository
from core.repositories.json.json_user_repository import (
    JSONUserRepository,
)
from core.use_cases.register_user_use_case import RegisterUserUseCase


# Factory to create an instance of RegisterUserUseCase
def execute() -> RegisterUserUseCase:
    user_repository = JSONUserRepository()
    role_repository = JSONRoleRepository()
    use_case = RegisterUserUseCase(user_repository, role_repository)

    return use_case