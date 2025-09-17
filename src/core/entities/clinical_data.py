from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(kw_only=True)
class ClinicalData:
    id: str = field(default_factory=lambda: str(uuid4()))
    data_type: str
    value: str
    unit: str
    description: str
    user_id: str
    patient_id: str
    version: int = 1
    active: bool = True
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
