import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(kw_only=True)
class EducationModule:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str
    description: str
    content: str
    quiz: dict
    created_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
