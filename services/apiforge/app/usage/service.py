import uuid

from app.models.api_usage import (
    APIUsage
)

from app.usage.repository import (
    UsageRepository
)


class UsageService:

    def __init__(
        self,
        repository: UsageRepository
    ):
        self.repository = repository

    async def log_request(
        self,
        api_key_id: uuid.UUID,
        endpoint: str,
        method: str,
        status_code: int,
        latency_ms: int
    ):

        usage = APIUsage(
            api_key_id=api_key_id,
            endpoint=endpoint,
            method=method,
            status_code=status_code,
            latency_ms=latency_ms
        )

        return await self.repository.create(
            usage
        )