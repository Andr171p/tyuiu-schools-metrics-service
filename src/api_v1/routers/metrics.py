from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.database.services.school import school_service
from src.database.services.direction import direction_service

from src.api_v1.schemas.metrics import GetMetricResponse
from src.metrics import school_metrics


metrics_router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)


@metrics_router.get(path="/school/{school_id}/", response_model=GetMetricResponse)
async def get_school_metrics(school_id: int) -> JSONResponse:
    school = await school_service.get_school_with_applicants(school_id)
    if len(school.applicants) < 10:
        raise HTTPException(
            ...
        )
    directions = await direction_service.get_directions_by_school_id(school_id)
    ...
