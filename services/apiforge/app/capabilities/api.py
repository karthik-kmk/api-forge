import uuid

from fastapi import (
    APIRouter,
    Depends,
    status
)

from app.models.user import User

from app.auth.dependencies import (
    get_current_user
)

from app.capabilities.schemas import (
    CreateCapabilityRequest,
    CapabilityResponse
)

from app.capabilities.service import (
    CapabilityService
)

from app.capabilities.dependencies import (
    get_capability_service
)


router = APIRouter(
    prefix="/capabilities",
    tags=["Capabilities"]
)


@router.post(
    "",
    response_model=CapabilityResponse,
    status_code=status.HTTP_201_CREATED
)
async def create_capability(
    request: CreateCapabilityRequest,
    service: CapabilityService = Depends(
        get_capability_service
    ),
    current_user: User = Depends(
        get_current_user
    )
):
    return await service.create_capability(
        name=request.name,
        slug=request.slug,
        description=request.description,
        endpoint=request.endpoint
    )


@router.get(
    "",
    response_model=list[CapabilityResponse]
)
async def list_capabilities(
    service: CapabilityService = Depends(
        get_capability_service
    ),
    current_user: User = Depends(
        get_current_user
    )
):
    return await service.list_capabilities()


@router.get(
    "/{capability_id}",
    response_model=CapabilityResponse
)
async def get_capability(
    capability_id: uuid.UUID,
    service: CapabilityService = Depends(
        get_capability_service
    ),
    current_user: User = Depends(
        get_current_user
    )
):
    return await service.get_capability(
        capability_id
    )


@router.patch(
    "/{capability_id}/activate",
    response_model=CapabilityResponse
)
async def activate_capability(
    capability_id: uuid.UUID,
    service: CapabilityService = Depends(
        get_capability_service
    ),
    current_user: User = Depends(
        get_current_user
    )
):
    return await service.activate_capability(
        capability_id
    )


@router.patch(
    "/{capability_id}/deactivate",
    response_model=CapabilityResponse
)
async def deactivate_capability(
    capability_id: uuid.UUID,
    service: CapabilityService = Depends(
        get_capability_service
    ),
    current_user: User = Depends(
        get_current_user
    )
):
    return await service.deactivate_capability(
        capability_id
    )