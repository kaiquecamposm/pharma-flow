from abc import ABC, abstractmethod
from typing import List

from core.entities.module_certificate import ModuleCertificate


class ModuleCertificateRepository(ABC):
    """
    Interface for module certificate repository.
    Defines methods for adding and retrieving module certificates.
    """
    @abstractmethod
    def add(self, user_id: str, module_id: str) -> ModuleCertificate:
        pass

    @abstractmethod
    def get_by_user_and_module(self, user_id: str, module_id: str) -> ModuleCertificate:
        pass

    @abstractmethod
    def list_by_user(self, user_id: str) -> List[ModuleCertificate]:
        pass