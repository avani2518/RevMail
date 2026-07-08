from datetime import datetime, timedelta, timezone

from sqlalchemy.orm import Session

from app.repositories.email_repository import EmailRepository


class EmailService:

    @staticmethod
    def create_email(
        db: Session,
        sender_id,
        subject: str,
        body: str,
        to: list,
        delay_minutes: int,
    ):
        """
        Create a new scheduled email.
        """

        scheduled_at = datetime.now(timezone.utc) + timedelta(
            minutes=delay_minutes
        )

        email = EmailRepository.create_email(
            db=db,
            sender_id=sender_id,
            scheduled_at=scheduled_at,
        )

        EmailRepository.create_email_version(
            db=db,
            email_id=email.id,
            subject=subject,
            body=body,
        )

        EmailRepository.create_recipients(
            db=db,
            email_id=email.id,
            recipients=to,
            recipient_type="TO",
        )

        return email

    @staticmethod
    def create_new_version(
        db: Session,
        email_id,
        subject: str,
        body: str,
    ):
        """
        Create another version of an email.
        """
        return EmailRepository.create_new_version(
            db=db,
            email_id=email_id,
            subject=subject,
            body=body,
        )

    @staticmethod
    def get_all_versions(
        db: Session,
        email_id,
    ):
        """
        Return all versions of an email.
        """
        return EmailRepository.get_all_versions(
            db=db,
            email_id=email_id,
        )

    @staticmethod
    def edit_email(
        db: Session,
        email_id,
        subject: str,
        body: str,
    ):
        """
        Edit an email by creating a new version.
        """
        return EmailRepository.create_new_version(
            db=db,
            email_id=email_id,
            subject=subject,
            body=body,
        )

    @staticmethod
    def get_user_emails(
        db: Session,
        user_id,
    ):
        """
        Return all emails created by a user.
        """
        return EmailRepository.get_user_emails(
            db=db,
            user_id=user_id,
        )

    @staticmethod
    def get_email(
        db: Session,
        email_id,
    ):
        """
        Return a single email.
        """
        return EmailRepository.get_email_by_id(
            db=db,
            email_id=email_id,
        )

    @staticmethod
    def get_pending_emails(
        db: Session,
    ):
        """
        Return all emails that are ready to be sent.
        """
        return EmailRepository.get_pending_emails(
            db=db,
        )