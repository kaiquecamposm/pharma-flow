from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional

from core.entities.base import BaseEntity


@dataclass
class EnvironmentalIndicator(BaseEntity):
    cycle_id: str = ""
    metric_name: str = ""
    value: float = 0.0
    unit: str = ""
    recorded_at: datetime = field(default_factory=datetime.utcnow)
    audited_by: Optional[str] = None
    audit_date: Optional[datetime] = None