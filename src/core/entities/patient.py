from dataclasses import dataclass
from datetime import date

from core.entities.base import BaseEntity
from core.entities.clinical_data import ClinicalData


@dataclass
class Patient(BaseEntity):
    full_name: str
    email: str
    dob: date
    gender: str
    clinical_history: list[ClinicalData] = None
    active: bool = True