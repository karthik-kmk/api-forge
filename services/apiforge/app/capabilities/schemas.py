import uuid

from datetime import datetime

from pydantic import BaseModel


class CreateCapabilityRequest(BaseModel):
    name: str
    slug: str
    description: str | None = None
    endpoint: str


class CapabilityResponse(BaseModel):
    id: uuid.UUID
    name: str
    slug: str
    description: str | None
    endpoint: str
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = {
        "from_attributes": True
    }