from core.entities.module_certificate import ModuleCertificate
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.module_certificate_repository import ModuleCertificateRepository


class GenerateModuleCertificateUseCase:
    def __init__(self, module_certificate_repository: ModuleCertificateRepository, audit_log_repository: AuditLogRepository):
        self.module_certificate_repository = module_certificate_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id: str, module_id: str) -> ModuleCertificate:
        """
        Generate a module certificate for the given user and module.
        """
        has_certificate = self.module_certificate_repository.get_by_user_and_module(user_id, module_id)

        if has_certificate:
            return has_certificate
        
        module_certificate = self.module_certificate_repository.add(user_id, module_id)

        if not module_certificate:
            raise ValueError("Failed to generate module certificate.")

        self.audit_log_repository.add(
            user_id=user_id,
            action="GENERATE_MODULE_CERTIFICATE",
            target_id=module_certificate.id,
            target_type="ModuleCertificate",
            details=f"Module certificate generated for user {user_id} and module {module_id}."
        )

        return module_certificate
