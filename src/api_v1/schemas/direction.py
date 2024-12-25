from typing import Literal, List

from pydantic import BaseModel


class DirectionSchema(BaseModel):
    university: str
    reception: str
    direction: str
    order: str | None

    class Config:
        orm_mode = True
        from_attributes = True
        json_encoders = {}


class DirectionsContent(BaseModel):
    status: Literal["ok"] = "ok"
    directions: List[DirectionSchema]


class DirectionsResponse(BaseModel):
    data: DirectionsContent
