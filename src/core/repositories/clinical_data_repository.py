from abc import ABC, abstractmethod
from datetime import datetime
from typing import Dict, List

from core.entities.clinical_data import ClinicalData


class ClinicalDataRepository(ABC):
    """
    Interface for clinical data repository.
    Defines methods for adding and retrieving clinical data.
    """
    @abstractmethod
    def add(self, data_type: str, value: str, unit: str, description: str, user_id: str, patient_id: str) -> ClinicalData:
        pass

    @abstractmethod
    def update(self, id: str, user_id: str, data_type: str, value: str, unit: str, description: str) -> ClinicalData:
        pass
    
    @abstractmethod
    def get_by_id(self, clinical_data_id: str) -> ClinicalData:
        pass

    @abstractmethod
    def list_by_patient_id(self, patient_id: str) -> List[ClinicalData]:
        pass

    @abstractmethod
    def list_all(self) -> List[ClinicalData]:
        pass

    @abstractmethod
    def list_by_period(self, start_date: datetime, end_date: datetime) -> Dict[str, List[ClinicalData]]:
        pass
    
    @abstractmethod
    def inactivate(self, clinical_data_id: str) -> bool:
        pass

    @abstractmethod
    def inactivate_by_patient_id(self, patient_id: str) -> bool:
        pass