from fastapi import APIRouter
from fastapi import Depends

from app.models.api_key import APIKey

from app.core.api_key_auth import (
    get_current_api_key
)

from app.email_validation.schemas import (
    EmailVerificationRequest,
    EmailVerificationResponse
)

from app.email_validation.service import (
    EmailValidationService
)

from app.email_validation.dependencies import (
    get_email_validation_service
)


router = APIRouter(
    prefix="/v1/email",
    tags=["Email Validation"]
)


@router.post(
    "/verify",
    response_model=EmailVerificationResponse
)
async def verify_email(

    request: EmailVerificationRequest,

    api_key: APIKey = Depends(
        get_current_api_key
    ),

    service: EmailValidationService = Depends(
        get_email_validation_service
    )

):

    return await service.verify(
        request.email
    )