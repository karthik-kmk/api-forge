from uuid import UUID

from pydantic import BaseModel
from pydantic import EmailStr


class SignupRequest(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: UUID
    email: str

    model_config = {
        "from_attributes": True
    }
    
class LoginRequest(BaseModel):
    email: EmailStr
    password: str