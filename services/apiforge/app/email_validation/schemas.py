from pydantic import BaseModel, EmailStr


class EmailVerificationRequest(BaseModel):
    email: EmailStr


class EmailVerificationResponse(BaseModel):
    email: str
    valid_syntax: bool
    mx_found: bool
    disposable: bool
    is_valid: bool