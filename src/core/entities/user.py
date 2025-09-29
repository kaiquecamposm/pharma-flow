from dataclasses import dataclass

from core.entities.base import BaseEntity


@dataclass
class User(BaseEntity):
    email: str
    password: str
    full_name: str
    role_name: str
    active: bool
