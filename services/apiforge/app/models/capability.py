import uuid

from datetime import datetime

from sqlalchemy import (
    String,
    Text,
    DateTime
)

from sqlalchemy.orm import (
    Mapped,
    mapped_column
)

from sqlalchemy.dialects.postgresql import UUID

from app.db.base import Base


class Capability(Base):
    __tablename__ = "capabilities"

    id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    name: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    slug: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False
    )

    description: Mapped[str | None] = mapped_column(
        Text,
        nullable=True
    )

    endpoint: Mapped[str] = mapped_column(
        String(255),
        nullable=False
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="ACTIVE"
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        default=datetime.utcnow,
        onupdate=datetime.utcnow
    )