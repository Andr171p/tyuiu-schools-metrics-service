from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.database.metrics.school import SchoolMetrics
from src.api_v1.schemas.metrics import MetricSchema, MetricResponse
from src.config import settings


metrics_router = APIRouter(
    prefix=f"{settings.api.api_v1_prefix}/metrics",
    tags=["Metrics"]
)


@metrics_router.get(path="/school/{school_id}/", response_model=MetricResponse)
async def get_school_metrics(school_id: int) -> JSONResponse:
    service = SchoolMetrics(school_id)
    metrics = await service.get_metrics()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "metrics": MetricSchema(
                    **dict(zip(MetricSchema.model_fields.keys(), metrics))
                ).model_dump()
            }
        }
    )
