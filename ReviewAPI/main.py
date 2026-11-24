
from contextlib import asynccontextmanager
from fastapi import FastAPI

from database import create_tables
from routes.reviews import router as reviews_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="Review API",
    description="A REST API to manage and analyze play reviews.",
    lifespan=lifespan
)


app.include_router(reviews_router)


@app.get("/")
def root():
    return {
        "message": "Welcome to Review API"
    }
