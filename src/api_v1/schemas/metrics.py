from pydantic import BaseModel
from typing import List, Literal, Tuple


class MetricSchema(BaseModel):
    applicants_count: int
    students_count: int
    genders_count: List[Tuple[str, int]]
    olympiads_count: int
    avg_gpa: float
    avg_score: float
    top_universities: List[Tuple[str, int]]
    top_directions: List[Tuple[str, int]]


class MetricContent(BaseModel):
    status: Literal["ok"] = "ok"
    metrics: MetricSchema


class MetricResponse(BaseModel):
    data: MetricContent
