from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(kw_only=True)
class ProductionData:
    id: str = field(default_factory=lambda: str(uuid4()))
    quantity: float
    energy_consumption: float
    recovered_solvent_volume: float
    emissions: float
    user_id: str
    lote_id: str
    version: int = 1
    active: bool = True
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())