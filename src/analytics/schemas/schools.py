from pydantic import BaseModel


class TopCountSchool(BaseModel):
    id: int
    name: str
    count: int


class TopScoreSchool(BaseModel):
    id: int
    name: str
    score: float
    count: int


class TopGPASchool(BaseModel):
    id: int
    name: str
    gpa: float
    count: int
