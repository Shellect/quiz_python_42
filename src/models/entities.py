from pydantic import BaseModel
from datetime import datetime



class ServiceEntity(BaseModel):
    name: str
    url: str
    check_interval: int
    timeout: int
    expected_status: int
    created_at: datetime
    is_active: bool = True