import time

from starlette.middleware.base import (
    BaseHTTPMiddleware
)

from app.db.database import (
    AsyncSessionLocal
)

from app.usage.repository import (
    UsageRepository
)

from app.usage.service import (
    UsageService
)


class UsageMiddleware(
    BaseHTTPMiddleware
):

    async def dispatch(
        self,
        request,
        call_next
    ):

        start_time = time.time()

        response = await call_next(
            request
        )

        api_key = getattr(
            request.state,
            "api_key",
            None
        )

        if api_key:

            latency_ms = int(
                (time.time() - start_time)
                * 1000
            )

            async with AsyncSessionLocal() as db:

                repository = UsageRepository(
                    db
                )

                service = UsageService(
                    repository
                )

                await service.log_request(
                    api_key_id=api_key.id,
                    endpoint=request.url.path,
                    method=request.method,
                    status_code=response.status_code,
                    latency_ms=latency_ms
                )

        return response