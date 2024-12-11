from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import Mapped, mapped_column, declared_attr

from typing import TypeVar

from src.config import settings


def get_db_url(
        user: str = settings.postgres.user,
        password: str = settings.postgres.password,
        host: str = settings.postgres.host,
        port: int = settings.postgres.port,
        database: str = settings.postgres.database
) -> str:
    return f"postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}"


class Base(AsyncAttrs, DeclarativeBase):
    __abstract__ = True

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return f"{cls.__name__.lower()}s"

    id: Mapped[int] = mapped_column(
        autoincrement=True,
        primary_key=True
    )


ModelType = TypeVar("ModelType", bound=Base)
