from abc import ABC, abstractmethod

from core.entities.education_progress import EducationProgress


class EducationProgressRepository(ABC):
    """
    Interface for education progress repository.
    Defines methods for adding and retrieving education progress.
    """
    @abstractmethod
    def add(self, user_id: str, module_id: str) -> EducationProgress:
        pass

    @abstractmethod
    def get_by_id(self, education_progress_id: str) -> EducationProgress:
        pass

    @abstractmethod
    def get_by_user_and_module(self, user_id: str, module_id: str) -> EducationProgress:
        pass

    @abstractmethod
    def list_by_user_id(self, user_id: str) -> list[EducationProgress]:
        pass

    @abstractmethod
    def update(self, education_progress_id: str, completed: bool, completed_at: str, score: int) -> EducationProgress:
        pass