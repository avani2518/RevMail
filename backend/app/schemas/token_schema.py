from pydantic import BaseModel, EmailStr


class UserLogin(BaseModel):
    """
    Request body for user login.
    """
    email: EmailStr
    password: str


class Token(BaseModel):
    """
    Response returned after successful login.
    """
    access_token: str
    token_type: str