from fastapi import APIRouter, Query, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.config import settings
from src.database.services.school import school_service
from src.api_v1.middlewares.globals import g
from src.api_v1.schemas.school import (
    SchoolSchema,
    GetSchoolResponse,
    GetSchoolsResponse,
    SearchSchoolsResponse
)


school_router = APIRouter(
    prefix=f"{settings.api.api_v1_prefix}/schools",
    tags=["Schools"]
)


@school_router.get(path="/get/schools/{school_id}/", response_model=GetSchoolResponse)
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


@school_router.get(path="/get/schools/", response_model=GetSchoolsResponse)
async def get_schools() -> JSONResponse:
    schools = await school_service.get_schools()
    schools_schemas = [SchoolSchema.from_orm(school).dict() for school in schools]
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "schools": schools_schemas
            }
        }
    )


@school_router.get(path="/search/", response_model=SearchSchoolsResponse)
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
