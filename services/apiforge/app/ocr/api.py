from fastapi import (
    APIRouter,
    Depends,
    UploadFile,
    File
)

from app.ocr.schemas import (
    OCRResponse
)

from app.ocr.service import (
    OCRService
)

from app.ocr.dependencies import (
    get_ocr_service
)

from app.core.api_key_auth import (
    get_current_api_key
)

from app.models.api_key import (
    APIKey
)
router = APIRouter(
    prefix="/v1/ocr",
    tags=["OCR"]
)


@router.post(
    "/extract",
    response_model=OCRResponse
)
async def extract_text(
    file: UploadFile = File(...),
    service: OCRService = Depends(
        get_ocr_service
    ),
    api_key: APIKey = Depends(
        get_current_api_key
    )
):

    text = await service.extract_text(
        file
    )

    return OCRResponse(
        text=text
    )