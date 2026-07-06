from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """
    Handles all database operations related to users.
    """

    @staticmethod
    def get_by_email(db: Session, email: str):
        """
        Return a user if the email already exists.
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
    ):
        """
        Create and save a new user.
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