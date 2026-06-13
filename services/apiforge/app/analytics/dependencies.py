from fastapi import Depends

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.database import (
    get_db
)

from app.analytics.repository import (
    AnalyticsRepository
)

from app.analytics.service import (
    AnalyticsService
)


def get_analytics_service(
    db: AsyncSession = Depends(
        get_db
    )
):

    repository = AnalyticsRepository(
        db
    )

    return AnalyticsService(
        repository
    )