from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db

from app.capabilities.repository import (
    CapabilityRepository
)

from app.capabilities.service import (
    CapabilityService
)


def get_capability_service(
    db: AsyncSession = Depends(get_db)
) -> CapabilityService:

    repository = CapabilityRepository(
        db=db
    )

    return CapabilityService(
        repository=repository
    )