from dataclasses import dataclass

from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.education_module_repository import EducationModuleRepository
from core.repositories.education_progress_repository import EducationProgressRepository
from core.repositories.module_certificate_repository import ModuleCertificateRepository
from utils import console


@dataclass
class AccessEnvironmentalEducationModulesUseCase:
    def __init__(self, education_module_repository: EducationModuleRepository, education_progress_repository: EducationProgressRepository, module_certificate_repository: ModuleCertificateRepository, audit_log_repository: AuditLogRepository):
        self.education_module_repository = education_module_repository
        self.education_progress_repository = education_progress_repository
        self.module_certificate_repository = module_certificate_repository
        self.audit_log_repository = audit_log_repository

    
    def execute(self, user_id: str, module_id: str):
        """
        User accesses an environmental education module.

        Time Complexity Analysis:

        - Fetch module by ID:
            - O(M)
            (M = total number of modules if stored in a list; O(1) if indexed by dict)

        - Fetch progress by user and module:
            - O(P)
            (P = total number of progress records; O(1) if indexed by (user_id, module_id) tuple)

        - Add progress if not found:
            - O(1)

        - Check for certificate:
            - O(C)
            (C = total number of certificates; O(1) if indexed by (user_id, module_id))

        - Add certificate if needed:
            - O(1)

        - Audit log insertion:
            - O(1)

        Total Complexity:
            - O(M + P + C) in the worst case if repositories use lists
            - O(1) for each operation if repositories use proper indexing (dicts or maps)

        Best / Average / Worst Case:
            - Worst case: linear search through lists → O(M + P + C)
            - Best case (indexed structures): O(1)
        """

        try:
            module = self.education_module_repository.get_by_id(module_id)

            if not module:
                raise ValueError(f"Educational module {module_id} not found.")

            progress = self.education_progress_repository.get_by_user_and_module(user_id, module_id)

            if not progress:
                progress = self.education_progress_repository.add(user_id, module_id)

            if progress.score == 1:
                has_certificate = self.module_certificate_repository.get_by_user_and_module(user_id, module_id)

                if not has_certificate:
                    self.module_certificate_repository.add(user_id, module_id)

            self.audit_log_repository.add(
                user_id=user_id,
                action="ACCESS_MODULE",
                target_id=module_id,
                target_type="EducationModule, EducationProgress",
                details=f"User {user_id} accessed module '{module.title}'"
            )

            return {
                "module": module,
                "progress": progress
            }
        except Exception as e:
            console.io.print(f"[bold red]Failed to access educational module: {str(e)}[/bold red]")
            return None
