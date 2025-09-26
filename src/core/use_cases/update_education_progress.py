from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from core.entities.education_progress import EducationProgress
from core.repositories.audit_log_repository import AuditLogRepository
from core.repositories.education_progress_repository import EducationProgressRepository
from utils import console


@dataclass
class UpdateEducationProgressUseCase:
    def __init__(self, education_progress_repository: EducationProgressRepository, audit_log_repository: AuditLogRepository):
        self.education_progress_repository = education_progress_repository
        self.audit_log_repository = audit_log_repository

    def execute(self, user_id: str, module_id: str, score: int) -> Optional[EducationProgress]:
        try:
            education_progress = self.education_progress_repository.get_by_user_and_module(user_id, module_id)

            if not education_progress:
                raise ValueError(console.io.print("[bold red]Education progress record not found.[/bold red]"))

            updated_education_progress = self.education_progress_repository.update(education_progress.id, score > 0, datetime.now(timezone.utc).isoformat(), score)

            self.audit_log_repository.add({
                "user_id": user_id,
                "action": "UPDATE_EDUCATION_PROGRESS",
                "target_id": updated_education_progress.id,
                "target_type": "EducationProgress",
                "details": f"Updated education progress for module {module_id} with score {score}",
            })

            return updated_education_progress

        except Exception as e:
            raise console.io.print_exception(f"Failed to update education progress: {str(e)}")