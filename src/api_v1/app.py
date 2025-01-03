from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api_v1.lifespan import lifespan
from src.api_v1.routers import (
    applicant_router,
    school_router,
    metrics_router
)
from src.config import settings


app = FastAPI(
    title=settings.api.name,
    lifespan=lifespan
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(school_router)
app.include_router(metrics_router)
app.include_router(applicant_router)
