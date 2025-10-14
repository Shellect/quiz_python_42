import time
from datetime import datetime

import httpx

from src.models.entities import ServiceEntity
from src.models.schemas import ServiceStatus, ServiceHealth


async def check_all_services(service: ServiceEntity):
    try:
        start_time = time.time()

        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get("http://localhost:3000")
            response_time = time.time() - start_time

            if response.status_code == service.expected_status:
                status = ServiceStatus.UP
            elif response_time > service.timeout:
                status = ServiceStatus.SLOW
            else:
                status = ServiceStatus.DOWN

            health = ServiceHealth(
                name=service.name,
                url=service.url,
                status=status,
                response_time=response_time,
                last_checked=datetime.now(),
                status_code=response.status_code
            )
    except Exception as e:
        pass