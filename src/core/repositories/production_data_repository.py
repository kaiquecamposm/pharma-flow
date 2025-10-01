
from abc import ABC, abstractmethod
from datetime import datetime
from typing import List

from core.entities.production_data import ProductionData


class ProductionDataRepository(ABC):
    """
    Interface for production data repository.
    Defines methods for adding and retrieving production data.
    """
    @abstractmethod
    def add(self, quantity: int, energy_consumption: int, recovered_solvent_volume: int, emissions: int, user_id: str, lote_id: str) -> ProductionData:
        pass

    @abstractmethod
    def get_by_lote_id(self, lote_id: str) -> ProductionData:
        pass
    
    @abstractmethod
    def list_all(self) -> List[ProductionData]:
        pass
    
    @abstractmethod
    def list_by_period(self, start_date: datetime, end_date: datetime) -> List[ProductionData]:
        pass

    @abstractmethod
    def inactivate_by_lote_id(self, lote_id: str) -> None:
        pass