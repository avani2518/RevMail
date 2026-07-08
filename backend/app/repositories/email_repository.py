from datetime import datetime, timezone

from sqlalchemy.orm import Session

from app.models.email import Email
from app.models.email_version import EmailVersion
from app.models.recipient import Recipient


class EmailRepository:

    @staticmethod
    def create_email(
        db: Session,
        sender_id,
        scheduled_at=None,
    ):
        email = Email(
            sender_id=sender_id,
            scheduled_at=scheduled_at,
        )

        db.add(email)
        db.commit()
        db.refresh(email)

        return email

    @staticmethod
    def create_email_version(
        db: Session,
        email_id,
        subject: str,
        body: str,
    ):
        version = EmailVersion(
            email_id=email_id,
            version_number=1,
            subject=subject,
            body=body,
            is_current=True,
        )

        db.add(version)
        db.commit()
        db.refresh(version)

        return version

    @staticmethod
    def create_recipients(
        db: Session,
        email_id,
        recipients: list,
        recipient_type: str,
    ):
        recipient_objects = []

        for email in recipients:
            recipient = Recipient(
                email_id=email_id,
                recipient_email=email,
                recipient_type=recipient_type,
            )

            recipient_objects.append(recipient)

        db.add_all(recipient_objects)
        db.commit()

        return recipient_objects

    @staticmethod
    def get_current_version(
        db: Session,
        email_id,
    ):
        return (
            db.query(EmailVersion)
            .filter(
                EmailVersion.email_id == email_id,
                EmailVersion.is_current == True,
            )
            .first()
        )

    @staticmethod
    def create_new_version(
        db: Session,
        email_id,
        subject: str,
        body: str,
    ):
        current_version = EmailRepository.get_current_version(
            db=db,
            email_id=email_id,
        )

        if current_version:
            current_version.is_current = False
            version_number = current_version.version_number + 1
        else:
            version_number = 1

        new_version = EmailVersion(
            email_id=email_id,
            version_number=version_number,
            subject=subject,
            body=body,
            is_current=True,
        )

        db.add(new_version)
        db.commit()
        db.refresh(new_version)

        return new_version

    @staticmethod
    def get_all_versions(
        db: Session,
        email_id,
    ):
        return (
            db.query(EmailVersion)
            .filter(
                EmailVersion.email_id == email_id
            )
            .order_by(
                EmailVersion.version_number
            )
            .all()
        )

    @staticmethod
    def get_user_emails(
        db: Session,
        user_id,
    ):
        return (
            db.query(Email)
            .filter(
                Email.sender_id == user_id
            )
            .order_by(
                Email.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_email_by_id(
        db: Session,
        email_id,
    ):
        return (
            db.query(Email)
            .filter(
                Email.id == email_id
            )
            .first()
        )

    @staticmethod
    def get_pending_emails(
        db: Session,
    ):
        return (
            db.query(Email)
            .filter(
                Email.status == "pending",
                Email.scheduled_at <= datetime.now(timezone.utc),
            )
            .all()
        )