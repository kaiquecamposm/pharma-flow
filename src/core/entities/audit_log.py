import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass(kw_only=True)
class AuditLog:
    id: str = str(uuid.uuid4())
    user_id: str
    action: str
    target_id: str
    target_type: str
    timestamp: str = datetime.utcnow().isoformat()
    details: str = ""
