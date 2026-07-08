from app.database.database import SessionLocal
from app.repositories.email_repository import EmailRepository

db = SessionLocal()

email = EmailRepository.create_email(
    db=db,
    sender_id="b3d1cf1c-e71e-4c17-9096-87533537fc36"
)

print(email.id)

db.close()