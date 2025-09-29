from core.repositories.json.json_audit_log_repository import JSONAuditLogRepository
from core.repositories.json.json_module_certificate_repository import (
    JSONModuleCertificateRepository,
)
from core.use_cases.generate_module_certificate import GenerateModuleCertificateUseCase


# Factory to create an instance of GenerateModuleCertificateUseCase
def make_generate_module_certificate_use_case() -> GenerateModuleCertificateUseCase:
    module_certificate_repository = JSONModuleCertificateRepository()
    audit_log_repository = JSONAuditLogRepository()

    use_case = GenerateModuleCertificateUseCase(module_certificate_repository, audit_log_repository)

    return use_case