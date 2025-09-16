from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ClinicalData:
    patient_id: str
    data_type: str
    value: list
    user_id: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    version: int = 1
    active: bool = True