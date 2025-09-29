
from abc import ABC, abstractmethod

from core.entities.user import User


class UserRepository(ABC):
    """
    Interface for user repository.
    Defines methods for adding and retrieving users.
    """
    @abstractmethod
    def add(self, email: str, password: str, full_name: str, role_name: str, active: bool) -> User:
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: str) -> User:
        pass
    
    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass