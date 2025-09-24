from abc import ABC, abstractmethod

from core.entities.education_module import EducationModule


class EducationModuleRepository(ABC):
    """
    Interface for education module repository.
    Defines methods for adding and retrieving education modules.
    """
    @abstractmethod
    def get_by_id(self, education_module_id: str) -> EducationModule:
        pass

    @abstractmethod
    def list_all(self) -> list[EducationModule]:
        pass