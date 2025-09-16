from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass
class ProductionData:
    id: str = field(default_factory=lambda: str(uuid4()))
    energy_consumption: float
    recovered_solvent_volume: float
    emissions: float
    value: list
    version: int = 1
    active: bool = True
    user_id: str
    lote_id: str
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())