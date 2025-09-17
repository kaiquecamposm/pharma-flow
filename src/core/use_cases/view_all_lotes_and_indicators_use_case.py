from dataclasses import dataclass

from core.repositories.lote_repository import LoteRepository
from core.repositories.production_data_repository import ProductionDataRepository
from utils import console


@dataclass
class ViewAllLotesAndIndicatorsUseCase:
    def __init__(self, lotes_repository: LoteRepository, production_data_repository: ProductionDataRepository):
        self.lotes_repository = lotes_repository
        self.production_data_repository = production_data_repository
    def execute(self) -> list:
        """
        Retrieve all lotes along with their associated environmental indicators.
        """
        try:
            results = []

            lotes = self.lotes_repository.list_all()

            for lote in lotes:
                production_data = self.production_data_repository.get_by_lote_id(lote.id)

                results.append({
                    "id_lote": lote.id,
                    "product_name": lote.product_name,
                    "quantity": production_data.quantity if production_data else None,
                    "start_date": lote.start_date,
                    "end_date": lote.end_date,
                    "ambient_indicators": {
                        "emissions": production_data.emissions if production_data else None,
                        "energy_consumption": production_data.energy_consumption if production_data else None,
                        "recovered_solvent_volume": production_data.recovered_solvent_volume if production_data else None
                    },
                    "registration_date": production_data.timestamp if production_data else None
                })

            return results
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get lotes: {str(e)}[/bold red]")