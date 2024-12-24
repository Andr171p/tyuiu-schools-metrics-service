from pydantic import BaseModel


class TopSchool(BaseModel):
    id: int
    name: str
    count: int


class TopSchoolByScore(BaseModel):
    id: int
    name: str
    score: float
    count: int
