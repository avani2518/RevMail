import uuid

from sqlalchemy import Boolean, Column, DateTime, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func

from app.database.database import Base


class Recipient(Base):
    __tablename__ = "recipients"

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

    recipient_email = Column(
        String(255),
        nullable=False
    )

    recipient_type = Column(
        String(10),
        nullable=False
    )

    is_read = Column(
        Boolean,
        default=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )