import uuid
import logging

from app.models.capability import Capability

from app.capabilities.repository import CapabilityRepository

from app.capabilities.exceptions import (
    CapabilityAlreadyExistsException,
    CapabilityNotFoundException
)


logger = logging.getLogger(__name__)


class CapabilityService:

    def __init__(
        self,
        repository: CapabilityRepository
    ):
        self.repository = repository

    async def create_capability(
        self,
        name: str,
        slug: str,
        description: str | None,
        endpoint: str
    ) -> Capability:

        existing_name = await self.repository.get_by_name(
            name=name
        )

        if existing_name:
            raise CapabilityAlreadyExistsException()

        existing_slug = await self.repository.get_by_slug(
            slug=slug
        )

        if existing_slug:
            raise CapabilityAlreadyExistsException()

        capability = Capability(
            name=name,
            slug=slug,
            description=description,
            endpoint=endpoint
        )

        capability = await self.repository.create(
            capability
        )

        logger.info(
            "Capability created",
            extra={
                "capability_id": str(capability.id),
                "slug": capability.slug
            }
        )

        return capability

    async def list_capabilities(
        self
    ) -> list[Capability]:
        return await self.repository.get_all()

    async def get_capability(
        self,
        capability_id: uuid.UUID
    ) -> Capability:

        capability = await self.repository.get_by_id(
            capability_id
        )

        if not capability:
            raise CapabilityNotFoundException()

        return capability

    async def activate_capability(
        self,
        capability_id: uuid.UUID
    ) -> Capability:

        capability = await self.get_capability(
            capability_id
        )

        capability.status = "ACTIVE"

        capability = await self.repository.update(
            capability
        )

        logger.info(
            "Capability activated",
            extra={
                "capability_id": str(capability.id)
            }
        )

        return capability

    async def deactivate_capability(
        self,
        capability_id: uuid.UUID
    ) -> Capability:

        capability = await self.get_capability(
            capability_id
        )

        capability.status = "INACTIVE"

        capability = await self.repository.update(
            capability
        )

        logger.info(
            "Capability deactivated",
            extra={
                "capability_id": str(capability.id)
            }
        )

        return capability