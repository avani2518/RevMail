from pydantic import BaseModel


class EmailVersionCreate(BaseModel):
    subject: str
    body: str


class EmailVersionResponse(BaseModel):
    id: str
    version_number: int
    subject: str
    body: str
    is_current: bool

    class Config:
        from_attributes = True

class EmailEdit(BaseModel):
    subject: str
    body: str