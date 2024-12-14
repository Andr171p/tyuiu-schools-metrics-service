from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.database.metrics import SchoolMetrics

from src.api_v1.schemas.metrics import MetricSchema, GetMetricResponse


metrics_router = APIRouter(
    prefix="/metrics",
    tags=["Metrics"]
)


@metrics_router.get(path="/school/{school_id}/", response_model=GetMetricResponse)
async def get_school_metrics(school_id: int) -> JSONResponse:
    service = SchoolMetrics(school_id)
    metrics = {
        "applicants_count": await service.get_applicants_count(),
        "students_count": await service.get_students_count(),
        "genders_count": await service.get_genders_count(),
        "olympiads_count": await service.get_olympiads_count(),
        "avg_gpa": await service.get_avg_gpa(),
        "avg_score": await service.get_avg_score(),
        "top_universities": await service.get_top_universities(),
        "top_directions": await service.get_top_directions()
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "metrics": MetricSchema(**metrics)
            }
        }
    )
