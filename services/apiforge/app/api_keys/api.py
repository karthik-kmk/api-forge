from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db

from app.auth.dependencies import (
    get_current_user
)

from app.api_keys.schemas import (
    CreateAPIKeyRequest,
    CreateAPIKeyResponse
)

from app.api_keys.repository import (
    APIKeyRepository
)

from app.api_keys.service import (
    APIKeyService
)
from app.api_keys.schemas import( APIKeyResponse )

router = APIRouter(
    prefix="/api-keys",
    tags=["API Keys"]
)


@router.post(
    "",
    response_model=CreateAPIKeyResponse
)
async def create_api_key(
    request: CreateAPIKeyRequest,
    current_user=Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(
        get_db
    )
):

    repository = APIKeyRepository(
        db
    )

    service = APIKeyService(
        repository
    )

    api_key = await service.create_key(
        user_id=current_user.id,
        name=request.name
    )

    return {
        "api_key": api_key
    }
    
    
@router.get(
    "",
    response_model=list[APIKeyResponse]
)

async def list_api_keys(
    current_user=Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(
        get_db
    )
):

    repository = APIKeyRepository(
        db
    )

    service = APIKeyService(
        repository
    )

    return await service.list_keys(
        current_user.id
    )
    
    
@router.delete("/{api_key_id}")
async def revoke_api_key(
    api_key_id: str,
    current_user=Depends(
        get_current_user
    ),
    db: AsyncSession = Depends(
        get_db
    )
):

    repository = APIKeyRepository(
        db
    )

    service = APIKeyService(
        repository
    )

    result = await service.revoke_key(
        api_key_id=api_key_id,
        user_id=current_user.id
    )

    if not result:
        raise HTTPException(
            status_code=404,
            detail="API Key not found"
        )

    return {
        "message": "API key revoked"
    }