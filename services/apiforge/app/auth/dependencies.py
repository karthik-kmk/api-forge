from fastapi import Depends
from fastapi import HTTPException

from fastapi.security import HTTPBearer
from fastapi.security import HTTPAuthorizationCredentials

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db

from app.auth.repository import UserRepository

from app.core.security import (
    decode_access_token
)


security = HTTPBearer()


async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(
        security
    ),
    db: AsyncSession = Depends(get_db)
):

    payload = decode_access_token(
        credentials.credentials
    )

    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    user_id = payload.get("sub")

    repository = UserRepository(db)

    user = await repository.get_by_id(
        user_id
    )

    if not user:
        raise HTTPException(
            status_code=401,
            detail="User not found"
        )

    return user