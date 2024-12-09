from pathlib import Path
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"


class SQLiteSettings(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    echo: bool = True


class APISettings(BaseSettings):
    api_v1_prefix: str = "/api/v1"


class Settings(BaseSettings):
    api: APISettings = APISettings()
    db: SQLiteSettings = SQLiteSettings()


settings = Settings()
