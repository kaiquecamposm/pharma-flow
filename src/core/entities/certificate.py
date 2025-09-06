from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from core.entities.base import BaseEntity


@dataclass
class Certificate(BaseEntity):
    course_id: str = ""
    professional_id: str = ""
    issued_at: datetime = field(default_factory=datetime.utcnow)
    passed: bool = False
    score: Optional[float] = None