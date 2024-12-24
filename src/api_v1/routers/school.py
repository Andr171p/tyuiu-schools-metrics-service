from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.config import settings
from src.database.services.school import school_service
# from src.analytics.schemas import TopCountSchool, TopScoreSchool
from src.analytics import SchoolsAnalytics
from src.api_v1.middlewares.globals import g
from src.api_v1.schemas.school import SchoolSchema
from src.api_v1 import schemas


school_router = APIRouter(
    prefix=f"{settings.api.api_v1_prefix}/schools",
    tags=["Schools"]
)


@school_router.get(path="/", response_model=schemas.GetSchoolsResponse)
async def get_all_schools() -> JSONResponse:
    schools = await school_service.get_schools()
    schools_list = [SchoolSchema.from_orm(school).dict() for school in schools]
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "schools": schools_list
            }
        }
    )


@school_router.get(path="/{school_id}/", response_model=schemas.GetSchoolResponse)
async def get_school_by_id(school_id: int) -> JSONResponse:
    school = await school_service.get_school(school_id)
    if school is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"School with ID {school_id} not found"
        )
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "school": SchoolSchema(**school.__dict__).model_dump()
            }
        }
    )


@school_router.get(path="/search/", response_model=schemas.SearchSchoolsResponse)
async def search_schools(q: str = Query(...)) -> JSONResponse:
    search_service = g.search_service
    schools = await search_service.search(q)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "schools": schools
            }
        }
    )


@school_router.get(path="/top/count/{top_n}/", response_model=schemas.TopCountSchoolsResponse)
async def get_top_schools_by_applicants_count(top_n: int = 5) -> JSONResponse:
    schools_analytics = SchoolsAnalytics()
    schools = await schools_analytics.get_top_schools_by_count(top_n)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "schools": [
                    school.model_dump()
                    for school in schools
                ]
            }
        }
    )


@school_router.get(path="/top/score/{top_n}/", response_model=schemas.TopScoreSchoolsResponse)
async def get_top_schools_by_score(top_n: int = 5) -> JSONResponse:
    schools_analytics = SchoolsAnalytics()
    schools = await schools_analytics.get_top_schools_by_score(top_n)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "schools": [
                    school.model_dump()
                    for school in schools
                ]
            }
        }
    )
