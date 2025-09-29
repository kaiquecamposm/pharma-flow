import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class AuditLog:
    user_id: str
    action: str
    target_id: str
    target_type: str
    details: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    timestamp: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
