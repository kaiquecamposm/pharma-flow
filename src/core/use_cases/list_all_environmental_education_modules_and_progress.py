from dataclasses import dataclass

from core.entities.education_module import EducationModule
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.education_module_repository import EducationModuleRepository
from core.repositories.education_progress_repository import EducationProgressRepository
from utils import console


@dataclass
class ListAllEnvironmentalEducationModulesAndProgressUseCase:
    def __init__(self, education_module_repository: EducationModuleRepository, education_progress_repository: EducationProgressRepository, audit_log_repository: AuditLogRepository):
        self.education_module_repository = education_module_repository
        self.education_progress_repository = education_progress_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id) -> list[EducationModule]:
        """
        Get all environmental education modules and their progress.
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

            return modules
        except Exception as e:
            raise console.io.print(f"\n[bold red]Failed to get environmental education modules: {str(e)}[/bold red]")