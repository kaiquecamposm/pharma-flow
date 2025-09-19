from core.repositories.json.json_lote_repository import JSONLoteRepository
from core.repositories.json.json_production_data_repository import (
    JSONProductionDataRepository,
)
from core.use_cases.view_all_lotes_and_indicators_use_case import (
    ViewAllLotesAndIndicatorsUseCase,
)


# Factory to create an instance of ViewAllLotesAndIndicatorsUseCase
def make_view_all_lotes_and_indicators_use_case() -> ViewAllLotesAndIndicatorsUseCase:
    lote_repository = JSONLoteRepository()
    production_data_repository = JSONProductionDataRepository()

    use_case = ViewAllLotesAndIndicatorsUseCase(lote_repository, production_data_repository)

    return use_case