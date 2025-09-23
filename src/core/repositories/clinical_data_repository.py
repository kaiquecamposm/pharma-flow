from abc import ABC, abstractmethod
from datetime import datetime

from core.entities.clinical_data import ClinicalData


class ClinicalDataRepository(ABC):
    """
    Interface for clinical data repository.
    Defines methods for adding and retrieving clinical data.
    """
    @abstractmethod
    def add(self, clinical_data: ClinicalData) -> ClinicalData:
        pass

    @abstractmethod
    def update(self, id: str, user_id: str, data_type: str, value: str, unit: str, description: str) -> ClinicalData:
        pass
    
    @abstractmethod
    def get_by_id(self, clinical_data_id: str) -> ClinicalData:
        pass

    @abstractmethod
    def list_by_patient_id(self, patient_id: str) -> list[ClinicalData]:
        pass

    @abstractmethod
    def list_all(self) -> list[ClinicalData]:
        pass

    @abstractmethod
    def list_by_period(self, start_date: datetime, end_date: datetime) -> list[ClinicalData]:
        pass
    
    @abstractmethod
    def inactivate(self, clinical_data_id: str) -> None:
        pass