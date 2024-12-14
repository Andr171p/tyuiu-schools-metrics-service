from pydantic import BaseModel
from typing import List, Literal


class MetricSchema(BaseModel):
    applicants_count: int
    students_count: int
    avg_gpa: float
    avg_score: float
    popular_universities: List[str]
    popular_directions: List[str]


class GetMetricResponse(BaseModel):
    status: Literal["ok"] = "ok"
    metrics: MetricSchema
