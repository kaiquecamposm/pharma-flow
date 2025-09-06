from __future__ import annotations

from dataclasses import dataclass
from typing import Optional

from core.entities.base import BaseEntity


@dataclass
class ResearchCenter(BaseEntity):
    name: str = ""
    address: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    country: Optional[str] = None
    contact_email: Optional[str] = None
    phone: Optional[str] = None