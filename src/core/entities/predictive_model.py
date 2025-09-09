from dataclasses import dataclass, field
from datetime import date
from typing import Dict, Optional

from core.entities.base import BaseEntity


@dataclass
class PredictiveModel(BaseEntity):
    model_name: str = ""
    version_label: str = "1.0"
    training_date: Optional[date] = None
    metrics: Dict = field(default_factory=dict)
    limitations: Optional[str] = None
    approved_for_production: bool = False
    study_id: Optional[str] = None