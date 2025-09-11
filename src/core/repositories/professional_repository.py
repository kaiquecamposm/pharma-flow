
from abc import ABC, abstractmethod

from core.entities.professional import Professional


class ProfessionalRepository(ABC):
    """
    Interface for professional repository.
    Defines methods for adding and retrieving professionals.
    """
    @abstractmethod
    def add(self, professional: Professional) -> Professional:
        pass
    
    @abstractmethod
    def get_by_id(self, professional_id: str) -> Professional:
        pass
    
    @abstractmethod
    def list_all(self) -> list[Professional]:
        pass
    
    @abstractmethod
    def update(self, professional: Professional) -> Professional:
        pass
    
    @abstractmethod
    def inactivate(self, professional_id: str) -> None:
        pass