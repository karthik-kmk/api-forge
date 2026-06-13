from fastapi import (
    Header,
    Depends,
    Request
)

from sqlalchemy.ext.asyncio import (
    AsyncSession
)

from app.db.database import (
    get_db
)

from app.models.api_key import (
    APIKey
)

from app.api_keys.repository import (
    APIKeyRepository
)

from app.api_keys.exceptions import (
    InvalidAPIKeyException,
    InactiveAPIKeyException
)

from app.core.api_key import (
    hash_api_key
)


async def get_current_api_key(
    request: Request,
    x_api_key: str = Header(
        ...,
        alias="x-api-key"
    ),
    db: AsyncSession = Depends(
        get_db
    )
) -> APIKey:

    repository = APIKeyRepository(
        db
    )

    key_hash = hash_api_key(
        x_api_key
    )

    api_key = await repository.get_by_key_hash(
        key_hash
    )

    if not api_key:
        raise InvalidAPIKeyException()

    if not api_key.is_active:
        raise InactiveAPIKeyException()

    # Store for middleware access
    request.state.api_key = api_key

    return api_key