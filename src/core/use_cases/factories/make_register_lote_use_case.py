from core.repositories.json.json_lote_repository import JSONLoteRepository
from core.repositories.json.json_production_data_repository import (
    JSONProductionDataRepository,
)
from core.use_cases.register_lote import RegisterLoteUseCase


# Factory to create an instance of RegisterLoteUseCase
def execute() -> RegisterLoteUseCase:
    lote_repository = JSONLoteRepository()
    production_data_repository = JSONProductionDataRepository()

    use_case = RegisterLoteUseCase(lote_repository, production_data_repository)

    return use_case