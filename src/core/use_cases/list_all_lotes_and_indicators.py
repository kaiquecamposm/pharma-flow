from dataclasses import dataclass

from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.lote_repository import LoteRepository
from core.repositories.production_data_repository import ProductionDataRepository


@dataclass
class ListAllLotesAndIndicatorsUseCase:
    def __init__(self, lotes_repository: LoteRepository, production_data_repository: ProductionDataRepository, audit_log_repository: AuditLogRepository):
        self.lotes_repository = lotes_repository
        self.production_data_repository = production_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id) -> list:
        """
        Retrieve all lotes along with their associated environmental indicators.
        """
        try:
            results = []

            lotes = self.lotes_repository.list_all()

            for lote in lotes:
                production_data = self.production_data_repository.get_by_lote_id(lote.id)

                results.append({
                    "lote_id": lote.id,
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

            self.audit_log_repository.add(
                user_id=user_id,
                action="LIST_ALL_LOTES_AND_INDICATORS",
                target_id="*MULTIPLE*",
                target_type="Lote, ProductionData",
                details=f"Listed all lotes and their indicators. Total lotes: {len(results)}",
            )

            return results
        except Exception as e:
            raise Exception(f"\nFailed to get lotes: {str(e)}")