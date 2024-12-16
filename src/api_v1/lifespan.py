from fastapi import FastAPI

from contextlib import asynccontextmanager
from contextlib import AbstractAsyncContextManager

from src.config import settings
from src.search.service import ESService
from src.api_v1.middlewares.globals import g


@asynccontextmanager
async def lifespan(app: FastAPI) -> AbstractAsyncContextManager[None]:
    search_service = ESService(settings.es.index)
    g.set_default("search_service", search_service)
    yield
    del search_service
