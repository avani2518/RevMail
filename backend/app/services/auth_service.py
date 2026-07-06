from sqlalchemy.orm import Session
from fastapi import HTTPException, status

from app.core.security import hash_password
from app.repositories.user_repository import UserRepository
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

        # Check if email already exists
        existing_user = UserRepository.get_by_email(
            db,
            user.email
        )

        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered."
            )

        # Hash the password
        password_hash = hash_password(user.password)

        # Save user
        new_user = UserRepository.create(
            db=db,
            username=user.username,
            email=user.email,
            password_hash=password_hash,
        )

        return new_user