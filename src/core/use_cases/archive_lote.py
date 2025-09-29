from dataclasses import dataclass

from core.entities.lote import Lote
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.lote_repository import LoteRepository
from core.repositories.production_data_repository import ProductionDataRepository


@dataclass
class ArchiveLoteUseCase:
    def __init__(self, lote_repository: LoteRepository, production_data_repository: ProductionDataRepository, audit_log_repository: AuditLogRepository):
        self.lote_repository = lote_repository
        self.production_data_repository = production_data_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id, lote_id) -> Lote:
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

            self.audit_log_repository.add(
                user_id=user_id,
                action="ARCHIVE_LOTE",
                target_id=lote_id,
                target_type="Lote, ProductionData",
                details=f"Lote {lote_id} archived successfully.",
            )

            return lote_archived
        except Exception as e:
            raise ValueError(f"Failed to archive lote: {str(e)}")