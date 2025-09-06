from dataclasses import dataclass
from typing import Optional

from core.entities.base import BaseEntity


@dataclass
class PatientIdentifier(BaseEntity):
    patient_id: str = ""
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    medical_id: Optional[str] = None