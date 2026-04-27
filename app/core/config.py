"""Application settings loaded from environment variables via pydantic-settings."""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings from .env file."""

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")

    database_url: str = "postgresql+asyncpg://wallet:wallet@localhost:5432/wallet_db"
    pool_size: int = 5
    max_overflow: int = 5
    app_env: str = "development"


settings = Settings()
