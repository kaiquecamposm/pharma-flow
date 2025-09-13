
from abc import ABC, abstractmethod

from core.entities.role import Role


class RoleRepository(ABC):
    """
    Interface for role repository.
    Defines methods for adding and retrieving roles.
    """
    @abstractmethod
    def add(self, role: Role) -> Role:
        pass
    
    @abstractmethod
    def get_by_user_id(self, user_id: str) -> Role:
        pass

    @abstractmethod
    def list_all(self) -> list[Role]:
        pass