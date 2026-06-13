from fastapi import Depends

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.database import (
    get_db
)

from app.usage.repository import (
    UsageRepository
)

from app.usage.service import (
    UsageService
)


def get_usage_service(
    db: AsyncSession = Depends(
        get_db
    )
):

    repository = UsageRepository(
        db
    )

    return UsageService(
        repository
    )