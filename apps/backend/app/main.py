from fastapi import FastAPI

from app.api import api_router
from app.core.config import settings
from app.core.exceptions import register_exception_handlers
from app.core.logging import setup_logging
from app.core.request_id import RequestIDMiddleware

setup_logging()

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
)

app.add_middleware(RequestIDMiddleware)

register_exception_handlers(app)

app.include_router(api_router)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "OWL24 API",
    }
