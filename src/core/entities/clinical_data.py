from dataclasses import field
from datetime import datetime, timezone


class ClinicalData:
    patient_id: str
    data_type: str
    value: list
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    version: int = 1