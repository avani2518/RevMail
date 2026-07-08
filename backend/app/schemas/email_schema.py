from pydantic import BaseModel, EmailStr
from typing import List


class EmailCreate(BaseModel):
    subject: str
    body: str
    to: list[EmailStr]
    delay_minutes: int = 0