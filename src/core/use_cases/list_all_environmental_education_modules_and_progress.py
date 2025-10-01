from dataclasses import dataclass
from typing import List

from core.entities.education_module import EducationModule
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.education_module_repository import EducationModuleRepository
from core.repositories.education_progress_repository import EducationProgressRepository


@dataclass
class ListAllEnvironmentalEducationModulesAndProgressUseCase:
    def __init__(self, education_module_repository: EducationModuleRepository, education_progress_repository: EducationProgressRepository, audit_log_repository: AuditLogRepository):
        self.education_module_repository = education_module_repository
        self.education_progress_repository = education_progress_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id) -> List[EducationModule]:
        """
        List all education modules and user's progress.

        Time Complexity Analysis:

        - list_all() modules → O(n), n = number of modules
        - list_by_user_id(user_id) → O(p), p = number of progress entries for user
        - For each module, linear search in progress → O(n * p)
        - audit log insertion → O(1)

        Total Complexity: O(n * p)
        Best / Average / Worst Case: Linear in number of modules and user's progress entries (nested)
        """
        try:
            modules = self.education_module_repository.list_all()
            progress = self.education_progress_repository.list_by_user_id(user_id)

            for module in modules:
                module_progress = next((item for item in progress if item.module_id == module.id), None)
                if module_progress:
                    module.progress = module_progress.score * 100
                else:
                    module.progress = 0
                
            self.audit_log_repository.add(
                user_id=user_id,
                action="LIST_ENVIRONMENTAL_EDUCATION_MODULES_AND_PROGRESS",
                target_id="*MULTIPLE*",
                target_type="EducationModule, EducationProgress",
                details=f"Listed {len(modules)} environmental education modules with progress."
            )

            return modules
        except Exception as e:
            raise Exception(f"\nFailed to get environmental education modules: {str(e)}")