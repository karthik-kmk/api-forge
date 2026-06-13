import uuid

from datetime import datetime

from sqlalchemy import (
    String,
    Integer,
    DateTime,
    ForeignKey
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class APIUsage(Base):
    __tablename__ = "api_usage"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    api_key_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("api_keys.id")
    )

    endpoint: Mapped[str] = mapped_column(
        String(255)
    )

    method: Mapped[str] = mapped_column(
        String(20)
    )

    status_code: Mapped[int] = mapped_column(
        Integer
    )

    latency_ms: Mapped[int] = mapped_column(
        Integer
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )