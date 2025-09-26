from dataclasses import dataclass

from core.entities.lote import Lote
from core.entities.production_data import ProductionData
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.lote_repository import LoteRepository
from core.repositories.production_data_repository import ProductionDataRepository
from utils import console


@dataclass
class RegisterLoteUseCase:
    def __init__(self, lote_repository: LoteRepository, production_data_repository: ProductionDataRepository, audit_log_repository: AuditLogRepository):
        self.lote_repository = lote_repository
        self.production_data_repository = production_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, code: str, product_name: str, start_date: str, end_date: str, quantity: float, energy_consumption: float, emissions: float, recovered_solvent_volume: float, user_id: str) -> Lote:
        """
        Register a new lote.
        """
        try:
            new_lote = Lote(
                code=code,
                product_name=product_name,
                start_date=start_date,
                end_date=end_date,
                user_id=user_id,
            )

            new_production_data = ProductionData(
                quantity=quantity,
                energy_consumption=energy_consumption,
                recovered_solvent_volume=recovered_solvent_volume,
                emissions=emissions,
                user_id=user_id,
                lote_id=new_lote.id,
            )

            saved_lote = self.lote_repository.add(new_lote)
            saved_production_data = self.production_data_repository.add(new_production_data)

            if saved_lote and saved_production_data is None:
                raise ValueError("\n[bold red]Failed to register lote.[/bold red]")
            
            self.audit_log_repository.add({
                "user_id": user_id,
                "action": "REGISTER_LOTE",
                "target_id": new_lote.id,
                "target_type": "Lote, ProductionData",
                "details": f"Lote {new_lote.code} registered with production data.",
            })
                    
            return saved_lote
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to register lote: {str(e)}[/bold red]")