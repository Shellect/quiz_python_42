from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional


class ServiceStatus(Enum):
    UP = "up"
    DOWN = "down"
    SLOW = "slow"
    UNKNOWN = "unknown"

@dataclass
class ServiceHealth:
    name: str
    url: str
    status: ServiceStatus
    response_time: float
    last_checked: datetime
    status_code: Optional[int] = None
    error: Optional[str] = None