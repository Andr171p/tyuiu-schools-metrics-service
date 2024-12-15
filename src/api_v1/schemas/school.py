from pydantic import BaseModel
from typing import Literal, List


class SchoolSchema(BaseModel):
    id: int
    name: str
    city: str | None


class SchoolContent(BaseModel):
    status: Literal["ok"] = "ok"
    school: SchoolSchema


class SchoolsContent(BaseModel):
    status: Literal["ok"] = "ok"
    schools: List[SchoolSchema]


class GetSchoolResponse(BaseModel):
    data: SchoolContent


class GetSchoolsResponse(BaseModel):
    data: SchoolsContent
