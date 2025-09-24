import uuid
from dataclasses import dataclass, field
from datetime import datetime, timezone


@dataclass(kw_only=True)
class EducationProgress:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    user_id: str
    module_id: str
    started_at: str = field(default_factory=lambda: datetime.now(timezone.utc).isoformat())
    completed: bool = False
    completed_at: str = None
    score: int = 0
