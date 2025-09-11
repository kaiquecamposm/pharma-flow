from dataclasses import dataclass
from datetime import date
from typing import Dict, Optional

from core.entities.base import BaseEntity


@dataclass
class Patient(BaseEntity):
    def __init__(
        self,
        name: Optional[str] = None,
        dob: Optional[date] = None,
        gender: Optional[str] = None,
        demographics: Optional[Dict] = None,
        consent_signed: bool = False,
        consent_date: Optional[date] = None,
    ):
        self.name = name
        self.dob = dob
        self.gender = gender
        self.demographics = demographics
        self.consent_signed = consent_signed
        self.consent_date = consent_date
