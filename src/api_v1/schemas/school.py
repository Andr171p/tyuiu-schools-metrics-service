from pydantic import BaseModel
from typing import Literal, List


class SchoolSchema(BaseModel):
    id: int
    name: str
    city: str | None


class GetSchoolResponse(BaseModel):
    status: Literal["ok"] = "ok"
    school: SchoolSchema


class GetSchoolsResponse(BaseModel):
    status: Literal["ok"] = "ok"
    schools: List[SchoolSchema]
