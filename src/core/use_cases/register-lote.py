from dataclasses import dataclass

from core.entities.lote import Lote
from core.entities.production_data import ProductionData
from core.repositories.lote_repository import LoteRepository
from core.repositories.production_data_repository import ProductionDataRepository
from utils import console


@dataclass
class RegisterLoteUseCase:
    def __init__(self, lote_repository: LoteRepository, production_data_repository: ProductionDataRepository):
        self.lote_repository = lote_repository
        self.production_data_repository = production_data_repository

    def execute(self, lote_data: Lote, production_data: ProductionData) -> Lote:
        """
        Register a new lote.
        """
        try:
            new_lote = Lote(
                id=lote_data.id,
                code=lote_data.code,
                product_name=lote_data.product_name,
                start_date=lote_data.start_date,
                end_date=lote_data.end_date,
                user_id=lote_data.user_id,
            )

            saved_lote = self.lote_repository.add(new_lote)

            if saved_lote is None:
                raise ValueError("\n[bold red]Failed to register lote.[/bold red]")
            
            console.io.print("\n[bold green]Lote registered successfully![/bold green]")

            return saved_lote
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to register lote: {str(e)}[/bold red]")