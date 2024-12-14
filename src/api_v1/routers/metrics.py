import asyncio

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
    tasks = [
        service.get_applicants_count(),
        service.get_students_count(),
        service.get_genders_count(),
        service.get_olympiads_count(),
        service.get_avg_gpa(),
        service.get_avg_score(),
        service.get_top_universities(),
        service.get_top_directions()
    ]
    metrics = await asyncio.gather(*tasks)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "metrics": MetricSchema(*metrics)
            }
        }
    )
