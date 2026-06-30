from fastapi import FastAPI

app = FastAPI(
    title="owl24",
    version="0.1.0",
)


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Owl24 API"}