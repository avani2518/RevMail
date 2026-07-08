from fastapi import FastAPI

from app.api.v1.auth import router as auth_router
from app.api.v1.email import router as email_router
from app.scheduler.scheduler import scheduler

app = FastAPI(
    title="RevMail API",
    version="1.0.0"
)

# Start APScheduler
scheduler.start()

# Register routers
app.include_router(auth_router)
app.include_router(email_router)


@app.get("/")
def root():
    return {
        "message": "RevMail API is running!"
    }