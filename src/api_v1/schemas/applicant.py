from datetime import datetime
from typing import Literal, List

from pydantic import BaseModel


class ApplicantSchema(BaseModel):
    id: int
    full_name: str
    gender: str
    bdate: datetime
    gpa: float
    score: float
    olympiads: str | None

    class Config:
        orm_mode = True
        from_attributes = True
        json_encoders = {}


class ApplicantsContent:
    status: Literal["ok"] = "ok"
    applicants: List[ApplicantSchema]


class ApplicantsResponse(BaseModel):
    data: ApplicantsContent
