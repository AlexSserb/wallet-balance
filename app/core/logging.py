"""Logging configuration for the application."""

import logging
import sys

from app.core.config import settings

_LOG_FMT_DEV = "%(asctime)s | %(levelname)-8s | %(name)s - %(message)s"
_LOG_FMT_JSON = "%(asctime)s %(levelname)s %(name)s %(message)s"


def setup_logging() -> None:
    """Configure root logger level and format based on APP_ENV."""
    fmt = _LOG_FMT_JSON if settings.app_env == "production" else _LOG_FMT_DEV
    logging.basicConfig(
        level=logging.INFO,
        format=fmt,
        stream=sys.stdout,
        force=True,
    )
