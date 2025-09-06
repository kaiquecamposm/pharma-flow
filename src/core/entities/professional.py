from dataclasses import dataclass

from core.entities.base import BaseEntity


@dataclass
class Professional(BaseEntity):
    username: str = ""
    full_name: str = ""
    email: str = ""
    active: bool = True