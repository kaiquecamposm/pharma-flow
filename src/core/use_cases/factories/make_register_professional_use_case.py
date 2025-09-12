from core.repositories.json.json_professional_repository import (
    JSONProfessionalRepository,
)
from core.use_cases.register_professional_use_case import RegisterProfessionalUseCase


# Factory to create an instance of RegisterProfessionalUseCase
def execute() -> RegisterProfessionalUseCase:
    professional_repository = JSONProfessionalRepository()
    use_case = RegisterProfessionalUseCase(professional_repository)

    return use_case