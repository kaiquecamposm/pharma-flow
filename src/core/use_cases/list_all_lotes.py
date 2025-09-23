from dataclasses import dataclass

from core.entities.lote import Lote
from core.repositories.lote_repository import LoteRepository
from utils import console


@dataclass
class ListAllLotesUseCase:
    def __init__(self, lote_repository: LoteRepository):
        self.lote_repository = lote_repository

    def execute(self) -> list[Lote]:
        """
        Get all lotes data.
        """
        try:
            lotes = self.lote_repository.list_all()

            return lotes
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get lotes: {str(e)}[/bold red]")