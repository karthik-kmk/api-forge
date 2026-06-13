from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.auth.schemas import LoginRequest
from app.auth.schemas import (
    SignupRequest,
    UserResponse
)

from app.auth.repository import UserRepository
from app.auth.service import AuthService
from app.auth.dependencies import (
    get_current_user
)

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post(
    "/signup",
    response_model=UserResponse
)
async def signup(
    request: SignupRequest,
    db: AsyncSession = Depends(get_db)
):

    repository = UserRepository(db)

    service = AuthService(repository)

    user = await service.signup(
        email=request.email,
        password=request.password
    )

    return user


@router.post("/login")
async def login(
    request: LoginRequest,
    db: AsyncSession = Depends(get_db)
):

    repository = UserRepository(db)

    service = AuthService(repository)

    token = await service.login(
    email=request.email,
    password=request.password
)

    return {
    "access_token": token,
    "token_type": "bearer"
}
    
    

@router.get("/me")
async def me(
    current_user = Depends(
        get_current_user
    )
):
    return {
        "id": str(current_user.id),
        "email": current_user.email
    }