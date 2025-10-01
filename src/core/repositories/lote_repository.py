
from abc import ABC, abstractmethod
from typing import List

from core.entities.lote import Lote


class LoteRepository(ABC):
    """
    Interface for lote repository.
    Defines methods for adding and retrieving lotes.
    """
    @abstractmethod
    def add(self, code: str, product_name: str, start_date: str, end_date: str, user_id: str) -> Lote:
        pass
    
    @abstractmethod
    def list_all(self) -> List[Lote]:
        pass

    @abstractmethod
    def inactivate(self, lote_id: str) -> bool:
        pass