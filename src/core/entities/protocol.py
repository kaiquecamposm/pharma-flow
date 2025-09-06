from dataclasses import dataclass
from typing import Optional

from core.entities.base import BaseEntity


@dataclass
class Protocol(BaseEntity):
    protocol_id: str = ""
    title: str = ""
    version_label: str = "1.0"
    sponsor: Optional[str] = None
    ethics_committee_approval_id: Optional[str] = None
    approved: bool = False
    summary: Optional[str] = None