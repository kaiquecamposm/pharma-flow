
from abc import ABC, abstractmethod

from core.entities.user import User


class UserRepository(ABC):
    """
    Interface for user repository.
    Defines methods for adding and retrieving users.
    """
    @abstractmethod
    def add(self, user: User) -> User:
        pass
    
    @abstractmethod
    def get_by_id(self, user_id: str) -> User:
        pass
    
    @abstractmethod
    def get_by_email(self, email: str) -> User:
        pass

    @abstractmethod
    def list_all(self) -> list[User]:
        pass
    
    @abstractmethod
    def update(self, user: User) -> User:
        pass
    
    @abstractmethod
    def inactivate(self, user_id: str) -> None:
        pass