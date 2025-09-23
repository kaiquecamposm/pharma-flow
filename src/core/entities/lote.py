from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import uuid4


@dataclass(kw_only=True)
class Lote:
    id: str = field(default_factory=lambda: str(uuid4()))
    code: str
    product_name: str
    start_date: str
    end_date: str
    user_id: str
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    active: bool = True