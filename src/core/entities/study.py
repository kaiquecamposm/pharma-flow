from dataclasses import dataclass
from datetime import date
from typing import Optional

from core.entities.base import BaseEntity


@dataclass
class Study(BaseEntity):
    study_code: str = ""
    title: str = ""
    protocol_id: Optional[str] = None
    status: str = "draft"   # draft, ongoing, closed
    principal_investigator_id: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None