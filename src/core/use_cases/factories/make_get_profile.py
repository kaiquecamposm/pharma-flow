from core.repositories.json.json_user_repository import JSONUserRepository
from core.use_cases.get_profile import GetProfileUseCase


# Factory to create an instance of GetProfileUseCase
def make_get_profile_use_case() -> GetProfileUseCase:
    user_repository = JSONUserRepository()
    
    use_case = GetProfileUseCase(user_repository)

    return use_case