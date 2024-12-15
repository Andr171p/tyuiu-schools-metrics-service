from pydantic import BaseModel
from typing import Literal, List


class SchoolSchema(BaseModel):
    id: int
    name: str
    city: str | None


class SchoolResponse(BaseModel):
    status: Literal["ok"] = "ok"
    school: SchoolSchema


class SchoolsResponse(BaseModel):
    status: Literal["ok"] = "ok"
    schools: List[SchoolSchema]


class GetSchoolResponse(BaseModel):
    data: SchoolResponse


class GetSchoolsResponse(BaseModel):
    data: SchoolsResponse
