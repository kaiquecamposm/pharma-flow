from core.repositories.json.json_professional_repository import (
    JSONProfessionalRepository,
)
from core.use_cases.verify_credentials_use_case import VerifyCredentialsUseCase


# Factory to create an instance of VerifyCredentialsUseCase
def execute() -> VerifyCredentialsUseCase:
    professional_repository = JSONProfessionalRepository()
    use_case = VerifyCredentialsUseCase(professional_repository)

    return use_case