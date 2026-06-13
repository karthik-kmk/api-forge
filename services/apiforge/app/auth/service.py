from app.models.user import User

from app.core.security import (
    hash_password,
    verify_password,
    create_access_token
)

from app.auth.repository import UserRepository

from app.auth.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException
)

from app.core.logging import logger


class AuthService:

    def __init__(
        self,
        repository: UserRepository
    ):
        self.repository = repository

    async def signup(
        self,
        email: str,
        password: str
    ):
        logger.info(
            f"Creating user with email={email}"
        )

        existing = await self.repository.get_by_email(
            email
        )

        if existing:
            raise UserAlreadyExistsException()

        user = User(
            email=email,
            password_hash=hash_password(password)
        )

        logger.info(
            f"User created successfully id={user.id}"
        )

        return await self.repository.create(user)

    async def login(
        self,
        email: str,
        password: str
    ):
        user = await self.repository.get_by_email(
            email
        )

        if not user:
            raise InvalidCredentialsException()

        if not verify_password(
            password,
            user.password_hash
        ):
            raise InvalidCredentialsException()

        token = create_access_token(
            {
                "sub": str(user.id),
                "email": user.email
            }
        )

        return token