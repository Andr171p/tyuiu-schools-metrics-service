from src import database
from src.config import config


def get_db__url() -> str:
    url: str = f"postgresql+asyncpg://{config.postgres.user}:{config.postgres.password}@{config.postgres.host}:{config.postgres.port}/{config.postgres.db}"
    return url


DB_URL: str = get_db__url()
