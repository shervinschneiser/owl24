from fastapi import FastAPI

from app.core.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {
        "message": "OWL24 API",
    }