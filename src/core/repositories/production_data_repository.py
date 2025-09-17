
from abc import ABC, abstractmethod

from core.entities.production_data import ProductionData


class ProductionDataRepository(ABC):
    """
    Interface for production data repository.
    Defines methods for adding and retrieving production data.
    """
    @abstractmethod
    def add(self, production_data: ProductionData) -> ProductionData:
        pass
    
    @abstractmethod
    def get_by_id(self, production_data_id: str) -> ProductionData:
        pass

    @abstractmethod
    def get_by_lote_id(self, lote_id: str) -> ProductionData:
        pass
    
    @abstractmethod
    def list_all(self) -> list[ProductionData]:
        pass
    
    @abstractmethod
    def update(self, production_data: ProductionData) -> ProductionData:
        pass
    
    @abstractmethod
    def inactivate(self, production_data_id: str) -> None:
        pass