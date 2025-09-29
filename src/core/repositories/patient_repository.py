
from abc import ABC, abstractmethod

from core.entities.patient import Patient


class PatientRepository(ABC):
    """
    Interface for user repository.
    Defines methods for adding and retrieving users.
    """
    @abstractmethod
    def add(self, user: Patient) -> Patient:
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: str) -> Patient:
        pass
    
    @abstractmethod
    def get_by_email(self, email: str) -> Patient:
        pass

    @abstractmethod
    def list_all(self) -> list[Patient]:
        pass
    
    @abstractmethod
    def update(self, user: Patient) -> Patient:
        pass
    
    @abstractmethod
    def inactivate(self, patient_id: str) -> bool:
        pass