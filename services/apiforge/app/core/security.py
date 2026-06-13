from passlib.context import CryptContext
from datetime import datetime
from datetime import timedelta
from datetime import UTC

from jose import jwt

from app.core.config import settings


from jose import JWTError

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def hash_password(
    password: str
) -> str:
    return pwd_context.hash(password)



def verify_password(
    plain_password: str,
    hashed_password: str
):
    return pwd_context.verify(
        plain_password,
        hashed_password
    )
    
    
def create_access_token(
    data: dict
):

    payload = data.copy()

    expire = (
        datetime.now(UTC)
        + timedelta(
            minutes=settings.access_token_expire_minutes
        )
    )

    payload["exp"] = expire

    return jwt.encode(
        payload,
        settings.jwt_secret,
        algorithm=settings.jwt_algorithm
    )
    
    
def decode_access_token(
    token: str
):

    try:
        payload = jwt.decode(
            token,
            settings.jwt_secret,
            algorithms=[
                settings.jwt_algorithm
            ]
        )

        return payload

    except JWTError:
        return None