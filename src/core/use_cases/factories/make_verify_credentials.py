from core.repositories.json.json_user_repository import (
    JSONUserRepository,
)
from core.use_cases.verify_credentials import VerifyCredentialsUseCase


# Factory to create an instance of VerifyCredentialsUseCase
def make_verify_credentials_use_case() -> VerifyCredentialsUseCase:
    user_repository = JSONUserRepository()
    
    use_case = VerifyCredentialsUseCase(user_repository)

    return use_case