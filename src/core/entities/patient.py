from dataclasses import dataclass, field
from datetime import date
from typing import Dict, Optional

from core.entities.base import BaseEntity


@dataclass
class Patient(BaseEntity):
    anonymized_id: str = ""
    dob: Optional[date] = None
    gender: Optional[str] = None
    demographics: Dict = field(default_factory=dict)
    consent_signed: bool = False
    consent_date: Optional[date] = None
