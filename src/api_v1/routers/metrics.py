from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.database.services.school import school_service
from src.database.services.direction import direction_service

from src.api_v1.schemas.metrics import MetricSchema, GetMetricResponse
from src.metrics import utils


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
    applicants = school.applicants
    directions = await direction_service.get_directions_by_school_id(school_id)
    metrics = MetricSchema(
        applicants_count=utils.get_applicants_count(applicants),
        students_count=utils.get_students_count(directions),
        avg_gpa=utils.get_avg_gpa(applicants),
        avg_score=utils.get_avg_score(applicants),
        popular_universities=utils.get_popular_universities(directions, 3),
        popular_directions=utils.get_popular_directions(directions, 3)
    )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "metrics": metrics
            }
        }
    )
