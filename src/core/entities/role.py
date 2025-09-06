from dataclasses import dataclass

from core.entities.base import BaseEntity


@dataclass
class Role(BaseEntity):
    role_name: str = ""