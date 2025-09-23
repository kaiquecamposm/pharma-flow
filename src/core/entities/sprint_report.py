import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(kw_only=True)
class SprintReport:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    start_date: datetime
    end_date: datetime
    generated_by: str  # User ID of the report generator
    generated_at: datetime
    regulatory_indicators: dict = field(default_factory=dict)
    environmental_indicators: dict = field(default_factory=dict)
