from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.core.jwt import create_access_token
from app.core.security import hash_password, verify_password
from app.repositories.user_repository import UserRepository
from app.schemas.token_schema import UserLogin
from app.schemas.user_schema import UserRegister


class AuthService:
    """
    Handles authentication-related business logic.
    """

    @staticmethod
    def register(db: Session, user: UserRegister):
        """
        Register a new user.
        """

        existing_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered."
            )

        password_hash = hash_password(user.password)

        new_user = UserRepository.create(
            db=db,
            username=user.username,
            email=user.email,
            password_hash=password_hash,
        )

        return new_user

    @staticmethod
    def login(db: Session, user: UserLogin):
        """
        Authenticate a user and return a JWT access token.
        """

        existing_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if not existing_user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        if not verify_password(
            user.password,
            existing_user.password_hash
        ):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password."
            )

        access_token = create_access_token(
            data={
                "sub": str(existing_user.id),
                "email": existing_user.email
            }
        )

        return {
            "access_token": access_token,
            "token_type": "bearer"
        }