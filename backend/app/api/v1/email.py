from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.dependencies.auth import get_current_user
from app.schemas.email_schema import EmailCreate
from app.schemas.email_version_schema import EmailVersionCreate, EmailEdit
from app.services.email_service import EmailService

router = APIRouter(
    prefix="/emails",
    tags=["Emails"],
)


@router.get("/me")
def current_user(
    user=Depends(get_current_user)
):
    return {
        "id": str(user.id),
        "username": user.username,
        "email": user.email,
    }


@router.post("/send")
def send_email(
    request: EmailCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    email = EmailService.create_email(
        db=db,
        sender_id=current_user.id,
        subject=request.subject,
        body=request.body,
        to=request.to,
        delay_minutes=request.delay_minutes,
    )

    return {
        "message": "Email scheduled successfully.",
        "email_id": str(email.id),
        "scheduled_at": email.scheduled_at,
    }


@router.post("/{email_id}/versions")
def create_new_version(
    email_id: str,
    request: EmailVersionCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    version = EmailService.create_new_version(
        db=db,
        email_id=email_id,
        subject=request.subject,
        body=request.body,
    )

    return {
        "message": "New version created successfully.",
        "version": version.version_number,
    }


@router.get("/{email_id}/versions")
def get_all_versions(
    email_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    versions = EmailService.get_all_versions(
        db=db,
        email_id=email_id,
    )

    return versions


@router.put("/{email_id}")
def edit_email(
    email_id: str,
    request: EmailEdit,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    version = EmailService.edit_email(
        db=db,
        email_id=email_id,
        subject=request.subject,
        body=request.body,
    )

    return {
        "message": "Email edited successfully.",
        "current_version": version.version_number,
    }


@router.get("/")
def get_my_emails(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    emails = EmailService.get_user_emails(
        db=db,
        user_id=current_user.id,
    )

    return emails


@router.get("/{email_id}")
def get_email(
    email_id: str,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    email = EmailService.get_email(
        db=db,
        email_id=email_id,
    )

    return email