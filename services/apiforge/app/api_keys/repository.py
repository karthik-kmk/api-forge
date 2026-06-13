from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.api_key import APIKey
from sqlalchemy import select

class APIKeyRepository:

    def __init__(
        self,
        db: AsyncSession
    ):
        self.db = db


    async def create(
        self,
        api_key: APIKey
    ):

        self.db.add(api_key)

        await self.db.commit()

        await self.db.refresh(api_key)

        return api_key


    async def get_by_user_id(
        self,
        user_id
    ):

        result = await self.db.execute(
            select(APIKey).where(
                APIKey.user_id == user_id
            )
        )

        return result.scalars().all()


    async def get_by_id(
        self,
        api_key_id
    ):

        result = await self.db.execute(
            select(APIKey).where(
                APIKey.id == api_key_id
            )
        )

        return result.scalar_one_or_none()


    async def update(
        self,
        api_key
    ):

        await self.db.commit()

        await self.db.refresh(api_key)

        return api_key
    
    async def get_by_key_hash(
        self,
        key_hash: str
    ) -> APIKey | None:

        result = await self.db.execute(
            select(APIKey).where(
                APIKey.key_hash == key_hash
            )
        )

        return result.scalar_one_or_none()