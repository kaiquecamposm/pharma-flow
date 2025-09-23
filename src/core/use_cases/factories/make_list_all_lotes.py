from core.repositories.json.json_lote_repository import JSONLoteRepository
from core.use_cases.list_all_lotes import ListAllLotesUseCase


# Factory to create an instance of ListAllLotesUseCase
def make_list_all_lotes_use_case() -> ListAllLotesUseCase:
    lote_repository = JSONLoteRepository()

    use_case = ListAllLotesUseCase(lote_repository)

    return use_case