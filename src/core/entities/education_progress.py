import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass
class EducationProgress:
    user_id: str
    module_id: str
    score: int = 0
    completed: bool = False
    completed_at: str = None
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    started_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
