from apscheduler.schedulers.background import BackgroundScheduler

from app.database.database import SessionLocal
from app.services.email_service import EmailService


def check_scheduled_emails():
    db = SessionLocal()

    try:
        emails = EmailService.get_pending_emails(db)

        print(f"Found {len(emails)} pending emails.")

        for email in emails:
            print(email.id)

    finally:
        db.close()


scheduler = BackgroundScheduler()

scheduler.add_job(
    check_scheduled_emails,
    "interval",
    seconds=30,
)