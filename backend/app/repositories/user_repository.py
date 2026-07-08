from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """
    Handles all database operations related to users.
    """

    @staticmethod
    def get_by_email(
        db: Session,
        email: str,
    ) -> User | None:
        """
        Return a user by email.
        """
        return (
            db.query(User)
            .filter(User.email == email)
            .first()
        )

    @staticmethod
    def create(
        db: Session,
        username: str,
        email: str,
        password_hash: str,
    ) -> User:
        """
        Create a new user.
        """
        user = User(
            username=username,
            email=email,
            password_hash=password_hash,
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user

    @staticmethod
    def get_by_id(
        db: Session,
        user_id,
    ) -> User | None:
        """
        Return a user by ID.
        """
        return (
            db.query(User)
            .filter(User.id == user_id)
            .first()
        )