import os
from pathlib import Path
from dotenv import load_dotenv
from pydantic_settings import BaseSettings


BASE_DIR: Path = Path(__file__).resolve().parent.parent

ENV_PATH: Path = BASE_DIR / ".env"

load_dotenv(dotenv_path=ENV_PATH)


class SQLiteSettings(BaseSettings):
    url: str = f"sqlite+aiosqlite:///{BASE_DIR}/db.sqlite3"
    echo: bool = True


class PostgreSQLSettings(BaseSettings):
    host: str = os.getenv("DB_HOST")
    port: int = os.getenv("DB_PORT")
    user: str = os.getenv("DB_USER")
    database: str = os.getenv("DB_DATABASE")
    password: str = os.getenv("DB_PASSWORD")


class DBSettings(BaseSettings):
    echo: bool = True


class ESSettings(BaseSettings):
    user: str = os.getenv("ES_USER")
    password: str = os.getenv("ES_PASSWORD")
    host: str = os.getenv("ES_HOST")
    port: int = os.getenv("ES_PORT")
    # url: str = f"https://{user}:{password}@{host}:{port}/"
    url: str = "https://elasticsearch-production-eeff.up.railway.app/"
    index: str = "schools"


class APISettings(BaseSettings):
    name: str = "tyuiu.metrics"
    api_v1_prefix: str = "/api/v1"


class Settings(BaseSettings):
    api: APISettings = APISettings()
    sqlite: SQLiteSettings = SQLiteSettings()
    postgres: PostgreSQLSettings = PostgreSQLSettings()
    db: DBSettings = DBSettings()
    es: ESSettings = ESSettings()


settings = Settings()
