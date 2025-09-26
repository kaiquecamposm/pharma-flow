from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_lote_repository import JSONLoteRepository
from core.repositories.json.json_production_data_repository import (
    JSONProductionDataRepository,
)
from core.use_cases.register_lote import RegisterLoteUseCase


# Factory to create an instance of RegisterLoteUseCase
def make_register_lote_use_case() -> RegisterLoteUseCase:
    lote_repository = JSONLoteRepository()
    production_data_repository = JSONProductionDataRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = RegisterLoteUseCase(lote_repository, production_data_repository, audit_log_repository)

    return use_case