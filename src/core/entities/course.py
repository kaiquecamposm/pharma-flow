
from dataclasses import dataclass
from typing import Optional

from core.entities.base import BaseEntity


@dataclass
class Course(BaseEntity):
    name: str = ""
    description: Optional[str] = None