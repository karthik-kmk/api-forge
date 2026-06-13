import uuid

from datetime import datetime

from sqlalchemy import (
    String,
    Boolean,
    ForeignKey,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class APIKey(Base):
    __tablename__ = "api_keys"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    user_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("users.id")
    )

    name: Mapped[str] = mapped_column(
        String(100)
    )

    key_hash: Mapped[str] = mapped_column(
        String(255)
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )