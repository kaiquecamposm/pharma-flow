from dataclasses import dataclass

from core.entities.professional import Professional
from core.repositories.professional_repository import (
    ProfessionalRepository,
)


@dataclass
class RegisterProfessionalUseCase:
    def __init__(self, professional_repository: ProfessionalRepository):
        self.professional_repository = professional_repository

    def execute(self, professional_data: Professional) -> Professional:
        """
        Register a new professional.
        Business rules:
        """
        try:
            new_professional = Professional(
                username=professional_data.username,
                full_name=professional_data.full_name,
                email=professional_data.email,
                role_name=professional_data.role_name,
                active=professional_data.active,
            )

            print(f"Registering professional: {new_professional}")
            
            saved_professional = self.professional_repository.add(new_professional)

            return saved_professional

        except Exception as e:
            raise Exception(f"Failed to register professional: {str(e)}")