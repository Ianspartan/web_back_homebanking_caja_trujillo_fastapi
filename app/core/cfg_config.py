"""Configuración general del Homebanking Caja Trujillo."""
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    # Base de datos
    DATABASE_URL: str

    # JWT
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 480

    # API
    PORT: int = 8002

    # Frontends permitidos
    CORS_ORIGINS: str = (
     "http://localhost:5173,"
     "http://localhost:5174,"
     "https://core-caja-trujillo.vercel.app,"
     "https://homebanking-caja-trujillo.vercel.app"
)

    @property
    def cors_origins_list(self) -> list[str]:
        return [
            origen.strip()
            for origen in self.CORS_ORIGINS.split(",")
            if origen.strip()
        ]


settings = Settings()