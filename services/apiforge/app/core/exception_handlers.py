from fastapi import Request
from fastapi.responses import JSONResponse

from app.auth.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException
)

from app.capabilities.exceptions import (
    CapabilityAlreadyExistsException,
    CapabilityNotFoundException
)

from app.ocr.exceptions import (
    UnsupportedFileTypeException,
    OCRProcessingException
)

from app.pdf.exceptions import (
    PDFGenerationException
)

from app.api_keys.exceptions import (
    InvalidAPIKeyException,
    InactiveAPIKeyException
)

async def user_exists_handler(
    request: Request,
    exc: UserAlreadyExistsException
):
    return JSONResponse(
        status_code=409,
        content={
            "message": "User already exists"
        }
    )


async def invalid_credentials_handler(
    request: Request,
    exc: InvalidCredentialsException
):
    return JSONResponse(
        status_code=401,
        content={
            "message": "Invalid credentials"
        }
    )
    
    
async def capability_exists_handler(
    request: Request,
    exc: CapabilityAlreadyExistsException
):
    return JSONResponse(
        status_code=409,
        content={
            "message": "Capability already exists"
        }
    )


async def capability_not_found_handler(
    request: Request,
    exc: CapabilityNotFoundException
):
    return JSONResponse(
        status_code=404,
        content={
            "message": "Capability not found"
        }
    )
    
    
async def unsupported_file_type_handler(
    request: Request,
    exc: UnsupportedFileTypeException
):
    return JSONResponse(
        status_code=400,
        content={
            "message": "Unsupported file type"
        }
    )


async def ocr_processing_handler(
    request: Request,
    exc: OCRProcessingException
):
    return JSONResponse(
        status_code=500,
        content={
            "message": "OCR processing failed"
        }
    )
    
    
async def pdf_generation_handler(
    request: Request,
    exc: PDFGenerationException
):
    return JSONResponse(
        status_code=500,
        content={
            "message": "PDF generation failed"
        }
    )
    
async def invalid_api_key_handler(
    request: Request,
    exc: InvalidAPIKeyException
):
    return JSONResponse(
        status_code=401,
        content={
            "message": "Invalid API Key"
        }
    )


async def inactive_api_key_handler(
    request: Request,
    exc: InactiveAPIKeyException
):
    return JSONResponse(
        status_code=401,
        content={
            "message": "API Key is inactive"
        }
    )