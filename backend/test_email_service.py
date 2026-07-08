from app.database.database import SessionLocal
from app.services.email_service import EmailService

db = SessionLocal()

email = EmailService.create_email(
    db=db,
    sender_id="b3d1cf1c-e71e-4c17-9096-87533537fc36",   # your user UUID
    subject="Welcome to RevMail",
    body="This is my first email.",
    to=[
        "rahul@gmail.com",
        "priya@gmail.com",
        "sneha@gmail.com"
    ]
)

print(email.id)

db.close()