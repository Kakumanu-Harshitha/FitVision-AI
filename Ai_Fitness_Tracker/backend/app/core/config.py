from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Optional
import os

class Settings(BaseSettings):
    # Safe Defaults
    PROJECT_NAME: str = "AI Fitness Tracker"
    API_V1_STR: str = "/api/v1"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7  # 7 days
    RESET_PASSWORD_TOKEN_EXPIRE_HOURS: int = 1
    
    # Mandatory Variables (Loaded from environment)
    SECRET_KEY: str
    GROQ_API_KEY: str
    GMAIL_SENDER_EMAIL: str
    GMAIL_APP_PASSWORD: str
    
    # Safe Defaults
    ALGORITHM: str = "HS256"
    
    # Database Settings
    DATABASE_URL: str
    USE_POSTGRES: bool = True
    DATABASE_HOSTNAME: Optional[str] = None
    DATABASE_PORT: Optional[int] = None
    DATABASE_NAME: Optional[str] = None
    DATABASE_USERNAME: Optional[str] = None
    DATABASE_PASSWORD: Optional[str] = None
    
    # Cache Settings
    REDIS_HOST: str = "localhost"
    REDIS_PORT: int = 6379
    REDIS_PASSWORD: Optional[str] = None
    REDIS_DB: int = 0
    
    # Platform
    WEB_BASE_URL: str = "http://localhost:3000"
    
    # OAuth Settings
    GOOGLE_CLIENT_ID: Optional[str] = None
    GOOGLE_CLIENT_SECRET: Optional[str] = None
    GOOGLE_REDIRECT_URI: Optional[str] = None
    APPLE_CLIENT_ID: Optional[str] = None
    APPLE_TEAM_ID: Optional[str] = None
    APPLE_KEY_ID: Optional[str] = None
    APPLE_PRIVATE_KEY: Optional[str] = None
    APPLE_REDIRECT_URI: Optional[str] = None

    def get_database_url(self, is_async: bool = False) -> str:
        if not self.DATABASE_URL:
             raise ValueError("DATABASE_URL must be set in the environment.")
             
        url = self.DATABASE_URL
        if is_async:
            if url.startswith("postgresql://"):
                return url.replace("postgresql://", "postgresql+asyncpg://")
            if url.startswith("sqlite:///"):
                return url.replace("sqlite:///", "sqlite+aiosqlite:///")
        return url

    model_config = SettingsConfigDict(
        env_file=os.path.abspath(os.path.join(os.path.dirname(__file__), "../../.env")),
        env_file_encoding='utf-8',
        extra='ignore'
    )

settings = Settings()
