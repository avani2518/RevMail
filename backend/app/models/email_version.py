import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, Text
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.database import Base


class EmailVersion(Base):
    __tablename__ = "email_versions"

    id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4
    )

    email_id = Column(
        UUID(as_uuid=True),
        ForeignKey("emails.id"),
        nullable=False
    )

    version_number = Column(
        Integer,
        nullable=False
    )

    subject = Column(
        Text,
        nullable=False
    )

    body = Column(
        Text,
        nullable=False
    )

    is_current = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )