from dataclasses import dataclass

from core.entities.professional import Professional
from core.repositories.professional_repository import (
    ProfessionalRepository,
)
from utils import console


@dataclass
class RegisterProfessionalUseCase:
    def __init__(self, professional_repository: ProfessionalRepository):
        self.professional_repository = professional_repository

    def execute(self, professional_data: Professional) -> Professional:
        # Register a new professional.
        try:
            new_professional = Professional(
                email=professional_data.email,
                password=professional_data.password,
                full_name=professional_data.full_name,
                role_name=professional_data.role_name,
                active=professional_data.active,
            )
            
            saved_professional = self.professional_repository.add(new_professional)

            if saved_professional is None:
                raise ValueError("[bold red]Failed to register professional.[/bold red]")

            return saved_professional
        except Exception as e:
            console.io.print(f"[bold red]Failed to register professional: {str(e)}[/bold red]")