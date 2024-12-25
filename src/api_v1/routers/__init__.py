__all__ = (
    "school_router",
    "metrics_router",
    "applicant_router"
)

from src.api_v1.routers.school import school_router
from src.api_v1.routers.metrics import metrics_router
from src.api_v1.routers.applicant import applicant_router