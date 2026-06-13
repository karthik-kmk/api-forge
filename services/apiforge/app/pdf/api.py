from fastapi import (
    APIRouter,
    Depends
)

from fastapi.responses import StreamingResponse

from app.pdf.schemas import PDFGenerateRequest
from app.pdf.service import PDFService
from app.pdf.dependencies import get_pdf_service

from app.core.api_key_auth import get_current_api_key
from app.models.api_key import APIKey


router = APIRouter(
    prefix="/v1/pdf",
    tags=["PDF"]
)


@router.post("/generate")
async def generate_pdf(
    request: PDFGenerateRequest,
    service: PDFService = Depends(
        get_pdf_service
    ),
    api_key: APIKey = Depends(
        get_current_api_key
    )
):

    pdf_buffer = await service.generate_pdf(
        title=request.title,
        content=request.content
    )

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=document.pdf"
        }
    )