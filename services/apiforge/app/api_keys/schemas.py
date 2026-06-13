from uuid import UUID
from datetime import datetime

from pydantic import BaseModel


class CreateAPIKeyRequest(BaseModel):
    name: str


class CreateAPIKeyResponse(BaseModel):
    api_key: str


class APIKeyResponse(BaseModel):
    id: UUID
    name: str
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }
    
    



class APIKeyResponse(BaseModel):
    id: UUID
    name: str
    is_active: bool
    created_at: datetime

    model_config = {
        "from_attributes": True
    }