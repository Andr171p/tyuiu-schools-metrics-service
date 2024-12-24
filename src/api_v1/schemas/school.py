from typing import Literal, List, Optional

from pydantic import BaseModel

from src.analytics.schemas import (
    TopCountSchool,
    TopScoreSchool,
    TopGPASchool,
    TopStudentsSchool
)


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


class TopCountSchoolsContent(BaseModel):
    status: Literal["ok"] = "ok"
    schools: List[TopCountSchool]


class TopScoreSchoolsContent(BaseModel):
    status: Literal["ok"] = "ok"
    schools: List[TopScoreSchool]


class TopGPASchoolsContent(BaseModel):
    status: Literal["ok"] = "ok"
    schools: List[TopGPASchool]


class TopStudentsSchoolsContent(BaseModel):
    status: Literal["ok"] = "ok"
    schools: List[TopStudentsSchool]


class GetSchoolResponse(BaseModel):
    data: SchoolContent


class GetSchoolsResponse(BaseModel):
    data: SchoolsContent


class SearchSchoolsResponse(BaseModel):
    data: SearchSchoolsContent


class TopCountSchoolsResponse(BaseModel):
    data: TopCountSchoolsContent


class TopScoreSchoolsResponse(BaseModel):
    data: TopScoreSchoolsContent


class TopGPASchoolsResponse(BaseModel):
    data: TopGPASchoolsContent


class TopStudentsSchoolsResponse(BaseModel):
    data: TopStudentsSchoolsContent
