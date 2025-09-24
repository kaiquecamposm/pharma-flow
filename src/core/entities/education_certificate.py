import uuid
from dataclasses import dataclass, field
from datetime import datetime


@dataclass(kw_only=True)
class EducationCertificate:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    module_id: str
    issued_at: datetime = field(default_factory=datetime.utcnow)
