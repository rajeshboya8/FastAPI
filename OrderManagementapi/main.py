
from contextlib import asynccontextmanager

from fastapi import FastAPI

from database import create_tables
from routes.orders import router as orders_router
from routes.stats import router as stats_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    create_tables()
    yield


app = FastAPI(
    title="Order Management API",
    description="API for managing orders and generating statistics",
    version="1.0.0",
    lifespan=lifespan,
)


app.include_router(orders_router)
app.include_router(stats_router)


@app.get("/health", tags=["Health"])
def health_check():
    return {"status": "healthy"}
