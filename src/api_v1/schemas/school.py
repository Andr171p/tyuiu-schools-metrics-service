from pydantic import BaseModel
from typing import Literal, List, Optional


class SchoolSchema(BaseModel):
    id: int
    name: str
    city: str | None

    class Config:
        orm_mode = True
        from_attributes = True
        json_encoders = {}


class SchoolContent(BaseModel):
    status: Literal["ok"] = "ok"
    school: SchoolSchema


class SchoolsContent(BaseModel):
    status: Literal["ok"] = "ok"
    schools: List[Optional[SchoolSchema]]


class SearchSchoolsContent(BaseModel):
    status: Literal["ok"] = "ok"
    schools: List[SchoolSchema]


class GetSchoolResponse(BaseModel):
    data: SchoolContent


class GetSchoolsResponse(BaseModel):
    data: SchoolsContent


class SearchSchoolsResponse(BaseModel):
    data: SearchSchoolsContent
