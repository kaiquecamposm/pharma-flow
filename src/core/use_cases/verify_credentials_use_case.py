from dataclasses import dataclass
from typing import Optional

from core.entities.professional import Professional
from core.repositories.professional_repository import ProfessionalRepository
from utils import console


@dataclass
class VerifyCredentialsUseCase:
    def __init__(self, professional_repository: ProfessionalRepository):
        self.professional_repository = professional_repository

    def execute(self, email: str, password: str) -> Optional[Professional]:
        """
        Verify user credentials.
        Business rules:
        - Check if the email exists in the repository.
        - Validate the provided password against the stored password.
        """
        try:
            professional = self.professional_repository.get_by_email(email)

            if professional and professional.password == password:
                return professional
            return None

        except Exception as e:
            raise console.io.print_exception(f"Failed to verify credentials: {str(e)}")