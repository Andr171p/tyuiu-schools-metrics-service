from datetime import datetime
from typing import Literal, List

from pydantic import BaseModel, field_validator


class ApplicantSchema(BaseModel):
    id: int
    full_name: str
    gender: str
    bdate: str
    gpa: float
    score: int
    olympiads: str | None

    class Config:
        orm_mode = True
        from_attributes = True
        json_encoders = {}

    @field_validator('bdate')
    def validate_bdate(cls, value: datetime | str) -> str:
        if isinstance(value, datetime):
            return value.isoformat()
        return value


class ApplicantContent(BaseModel):
    status: Literal["ok"] = "ok"
    applicant: ApplicantSchema


class ApplicantsContent(BaseModel):
    status: Literal["ok"] = "ok"
    applicants: List[ApplicantSchema]


class ApplicantResponse(BaseModel):
    data: ApplicantsContent


class ApplicantsResponse(BaseModel):
    data: ApplicantsContent
