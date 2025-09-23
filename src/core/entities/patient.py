from dataclasses import dataclass
from datetime import date

from core.entities.base import BaseEntity


@dataclass
class Patient(BaseEntity):
    full_name: str
    email: str
    dob: date
    gender: str
    active: bool = True