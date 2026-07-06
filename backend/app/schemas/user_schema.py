from uuid import UUID
from datetime import datetime

from pydantic import BaseModel, EmailStr, ConfigDict


# ----------------------------
# Request Schema
# ----------------------------

class UserRegister(BaseModel):
    username: str
    email: EmailStr
    password: str


# ----------------------------
# Response Schema
# ----------------------------

class UserResponse(BaseModel):
    id: UUID
    username: str
    email: EmailStr
    is_active: bool
    is_verified: bool
    created_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )