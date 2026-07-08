from app.database.database import SessionLocal
from app.repositories.email_repository import EmailRepository

db = SessionLocal()

email = EmailRepository.create_email(
    db=db,
    sender_id="b3d1cf1c-e71e-4c17-9096-87533537fc36"
)

version = EmailRepository.create_email_version(
    db=db,
    email_id=email.id,
    subject="Hello RevMail",
    body="This is Version 1."
)

print(email.id)
print(version.id)

db.close()