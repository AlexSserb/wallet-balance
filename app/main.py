"""FastAPI application entry point."""

import logging
from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logging import setup_logging

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None]:
    """Configure logging and manage application startup and shutdown."""
    setup_logging()
    logger.info("Application startup")
    yield
    logger.info("Application shutdown")


app = FastAPI(
    title="Wallet Balance API",
    version="1.0.0",
    lifespan=lifespan,
)


@app.get("/ping")
async def ping() -> dict[str, str]:
    """Check that the service is running."""
    return {"status": "ok"}
