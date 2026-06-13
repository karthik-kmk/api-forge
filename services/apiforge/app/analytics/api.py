from fastapi import (
    APIRouter,
    Depends
)

from app.analytics.schemas import (
    UsageSummaryResponse
)

from app.analytics.service import (
    AnalyticsService
)

from app.analytics.dependencies import (
    get_analytics_service
)

from app.auth.dependencies import (
    get_current_user
)

from app.models.user import (
    User
)

from app.analytics.schemas import (
    UsageSummaryResponse,
    TopCapabilityResponse,
    RequestVolumeResponse
)


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get(
    "/usage",
    response_model=UsageSummaryResponse
)
async def get_usage_summary(
    current_user: User = Depends(
        get_current_user
    ),
    service: AnalyticsService = Depends(
        get_analytics_service
    )
):

    return await service.get_usage_summary()


@router.get(
    "/top-capabilities",
    response_model=list[
        TopCapabilityResponse
    ]
)
async def get_top_capabilities(
    current_user: User = Depends(
        get_current_user
    ),
    service: AnalyticsService = Depends(
        get_analytics_service
    )
):

    return await service.get_top_capabilities()


@router.get(
    "/request-volume",
    response_model=list[
        RequestVolumeResponse
    ]
)
async def get_request_volume(
    current_user: User = Depends(
        get_current_user
    ),
    service: AnalyticsService = Depends(
        get_analytics_service
    )
):

    return await service.get_request_volume()