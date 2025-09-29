import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class ModuleCertificate:
    user_id: str
    module_id: str
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    issued_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
