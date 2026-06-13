from app.models.api_usage import (
    APIUsage
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)


class UsageRepository:

    def __init__(
        self,
        db: AsyncSession
    ):
        self.db = db

    async def create(
        self,
        usage: APIUsage
    ):

        self.db.add(
            usage
        )

        await self.db.commit()

        await self.db.refresh(
            usage
        )

        return usage