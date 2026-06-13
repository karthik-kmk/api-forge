import uuid

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from app.models.capability import Capability


class CapabilityRepository:

    def __init__(
        self,
        db: AsyncSession
    ):
        self.db = db

    async def create(
        self,
        capability: Capability
    ) -> Capability:
        self.db.add(capability)

        await self.db.commit()
        await self.db.refresh(capability)

        return capability

    async def get_by_id(
        self,
        capability_id: uuid.UUID
    ) -> Capability | None:
        result = await self.db.execute(
            select(Capability).where(
                Capability.id == capability_id
            )
        )

        return result.scalar_one_or_none()

    async def get_by_name(
        self,
        name: str
    ) -> Capability | None:
        result = await self.db.execute(
            select(Capability).where(
                Capability.name == name
            )
        )

        return result.scalar_one_or_none()

    async def get_by_slug(
        self,
        slug: str
    ) -> Capability | None:
        result = await self.db.execute(
            select(Capability).where(
                Capability.slug == slug
            )
        )

        return result.scalar_one_or_none()

    async def get_all(
        self
    ) -> list[Capability]:
        result = await self.db.execute(
            select(Capability)
        )

        return list(result.scalars().all())

    async def update(
        self,
        capability: Capability
    ) -> Capability:
        await self.db.commit()
        await self.db.refresh(capability)

        return capability