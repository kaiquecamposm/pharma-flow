
from abc import ABC, abstractmethod

from core.entities.lote import Lote


class LoteRepository(ABC):
    """
    Interface for lote repository.
    Defines methods for adding and retrieving lotes.
    """
    @abstractmethod
    def add(self, lote: Lote) -> Lote:
        pass
    
    @abstractmethod
    def get_by_id(self, lote_id: str) -> Lote:
        pass
    
    @abstractmethod
    def list_all(self) -> list[Lote]:
        pass
    
    @abstractmethod
    def update(self, lote: Lote) -> Lote:
        pass
    
    @abstractmethod
    def inactivate(self, lote_id: str) -> None:
        pass