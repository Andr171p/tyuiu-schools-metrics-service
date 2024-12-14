from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.api_v1.schemas.school import GetSchoolResponse, GetSchoolsResponse

from src.database.services.school import school_service


school_router = APIRouter(
    prefix="/schools",
    tags=["Schools"]
)


@school_router.get(path="/get/school/{school_id}/", response_model=GetSchoolResponse)
async def get_school(school_id: int) -> JSONResponse:
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
                "school": school
            }
        }
    )


@school_router.get(path="/get/schools/", response_model=GetSchoolsResponse)
async def get_schools() -> JSONResponse:
    schools = await school_service.get_schools()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "schools": schools
            }
        }
    )
