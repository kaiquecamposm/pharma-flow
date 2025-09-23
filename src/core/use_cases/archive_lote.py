from dataclasses import dataclass

from core.entities.lote import Lote
from core.repositories.lote_repository import LoteRepository
from core.repositories.production_data_repository import ProductionDataRepository


@dataclass
class ArchiveLoteUseCase:
    def __init__(self, lote_repository: LoteRepository, production_data_repository: ProductionDataRepository):
        self.lote_repository = lote_repository
        self.production_data_repository = production_data_repository

    def execute(self, lote_id) -> Lote:
        """
        Archive a lote.
        """
        try:
            lote_archived = self.lote_repository.inactivate(lote_id)

            if not lote_archived:
                raise ValueError("Lote not found")

            production_data_archived = self.production_data_repository.inactivate_by_lote_id(lote_id)

            if not production_data_archived:
                raise ValueError("Failed to inactivate production data")

            return lote_archived
        except Exception as e:
            raise ValueError(f"Failed to archive patient: {str(e)}")