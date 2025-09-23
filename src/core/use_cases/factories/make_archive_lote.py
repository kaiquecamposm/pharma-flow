from core.repositories.json.json_lote_repository import JSONLoteRepository
from core.repositories.json.json_production_data_repository import (
    JSONProductionDataRepository,
)
from core.use_cases.archive_lote import ArchiveLoteUseCase


# Factory to create an instance of ArchiveLoteUseCase
def make_archive_lote_use_case() -> ArchiveLoteUseCase:
    lote_repository = JSONLoteRepository()
    production_data_repository = JSONProductionDataRepository()

    use_case = ArchiveLoteUseCase(
        lote_repository=lote_repository,
        production_data_repository=production_data_repository
    )

    return use_case