from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.db.database import engine
from app.db.base import Base

# Models
from app.models.user import User
from app.models.api_key import APIKey
from app.models.capability import Capability
from app.models.api_usage import APIUsage
# Routers
from app.auth.api import router as auth_router
from app.api_keys.api import router as api_key_router
from app.capabilities.api import router as capability_router
from app.ocr.api import router as ocr_router

# Exceptions
from app.auth.exceptions import (
    UserAlreadyExistsException,
    InvalidCredentialsException
)
from app.core.usage_middleware import (
    UsageMiddleware
)
from app.capabilities.exceptions import (
    CapabilityAlreadyExistsException,
    CapabilityNotFoundException
)

from app.screenshot.api import router as screenshot_router
from app.ocr.exceptions import (
    UnsupportedFileTypeException,
    OCRProcessingException
)

# Exception Handlers
from app.core.exception_handlers import (
    user_exists_handler,
    invalid_credentials_handler,
    capability_exists_handler,
    capability_not_found_handler,
    unsupported_file_type_handler,
    ocr_processing_handler,
    pdf_generation_handler,
    invalid_api_key_handler,
    inactive_api_key_handler
)

from app.pdf.api import (
    router as pdf_router
)
from app.email_validation.api import (
    router as email_validation_router
)
from app.pdf.exceptions import (
    PDFGenerationException
)


from app.api_keys.exceptions import (
    InvalidAPIKeyException,
    InactiveAPIKeyException
)

from app.analytics.api import (
    router as analytics_router
)

@asynccontextmanager
async def lifespan(app: FastAPI):
    async with engine.begin() as conn:
        await conn.run_sync(
            Base.metadata.create_all
        )

    yield


app = FastAPI(
    title="APIForge",
    lifespan=lifespan
)
app.add_middleware(
    UsageMiddleware
)

# Routers
app.include_router(auth_router)

app.include_router(
    api_key_router
)
app.include_router(
    email_validation_router
)
app.include_router(
    capability_router
)

app.include_router(screenshot_router)

app.include_router(
    analytics_router
)
app.include_router(
    pdf_router
)
app.include_router(
    ocr_router
)

# Exception Handlers
app.add_exception_handler(
    UserAlreadyExistsException,
    user_exists_handler
)

app.add_exception_handler(
    InvalidCredentialsException,
    invalid_credentials_handler
)

app.add_exception_handler(
    InvalidAPIKeyException,
    invalid_api_key_handler
)

app.add_exception_handler(
    InactiveAPIKeyException,
    inactive_api_key_handler
)

app.add_exception_handler(
    PDFGenerationException,
    pdf_generation_handler
)
app.add_exception_handler(
    CapabilityAlreadyExistsException,
    capability_exists_handler
)

app.add_exception_handler(
    CapabilityNotFoundException,
    capability_not_found_handler
)

app.add_exception_handler(
    UnsupportedFileTypeException,
    unsupported_file_type_handler
)

app.add_exception_handler(
    OCRProcessingException,
    ocr_processing_handler
)


# Health Check
@app.get("/health")
async def health():
    return {
        "status": "healthy"
    }