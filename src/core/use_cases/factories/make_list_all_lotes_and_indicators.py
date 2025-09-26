from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_lote_repository import JSONLoteRepository
from core.repositories.json.json_production_data_repository import (
    JSONProductionDataRepository,
)
from core.use_cases.list_all_lotes_and_indicators import (
    ListAllLotesAndIndicatorsUseCase,
)


# Factory to create an instance of ListAllLotesAndIndicatorsUseCase
def make_list_all_lotes_and_indicators_use_case() -> ListAllLotesAndIndicatorsUseCase:
    lote_repository = JSONLoteRepository()
    production_data_repository = JSONProductionDataRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = ListAllLotesAndIndicatorsUseCase(lote_repository, production_data_repository, audit_log_repository)

    return use_case