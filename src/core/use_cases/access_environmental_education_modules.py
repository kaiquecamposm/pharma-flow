from dataclasses import dataclass

from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.education_module_repository import EducationModuleRepository
from core.repositories.education_progress_repository import EducationProgressRepository
from utils import console


@dataclass
class AccessEnvironmentalEducationModulesUseCase:
    def __init__(self, education_module_repository: EducationModuleRepository, education_progress_repository: EducationProgressRepository, audit_log_repository: AuditLogRepository):
        self.education_module_repository = education_module_repository
        self.education_progress_repository = education_progress_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id: str, module_id: str):
        """
        User accesses an environmental education module.
        """

        try:
            module = self.education_module_repository.get_by_id(module_id)

            if not module:
                raise ValueError(f"Educational module {module_id} not found.")

            progress = self.education_progress_repository.get_by_user_and_module(user_id, module_id)

            if not progress:
                progress = self.education_progress_repository.create(user_id, module_id)

            self.audit_log_repository.add({
                "user_id": user_id,
                "action": "ACCESS_MODULE",
                "target_id": module_id,
                "target_type": "EducationModule, EducationProgress",
                "details": f"User {user_id} accessed module '{module.title}'"
            })

            return {
                "module": module,
                "progress": progress
            }

        except Exception as e:
            console.io.print(f"[bold red]Failed to access educational module: {str(e)}[/bold red]")
            return None
