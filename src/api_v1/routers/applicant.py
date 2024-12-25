import json

from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import HTTPException

from src.config import settings
from src.utils.encoder import DatetimeJsonEncoder
from src.database.services.applicant import applicant_service
from src.api_v1.schemas.applicant import ApplicantSchema, ApplicantResponse, ApplicantsResponse
from src.api_v1.schemas.direction import DirectionSchema, DirectionsResponse


applicant_router = APIRouter(
    prefix=f"{settings.api.api_v1_prefix}/applicants",
    tags=["Applicants"]
)


@applicant_router.get(path="/{applicant_id}/", response_model=ApplicantResponse)
async def get_applicant_by_id(applicant_id: int) -> JSONResponse:
    applicant = await applicant_service.get_applicant(applicant_id)
    if applicant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Applicant with ID {applicant_id} not found"
        )
    # applicant_json = json.loads(json.dumps(applicant.__dict__, cls=DatetimeJsonEncoder))
    applicant.bdate = applicant.bdate.isoformat()
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "applicant": ApplicantSchema(**applicant.__dict__).model_dump()
            }
        }
    )


@applicant_router.get(path="/{applicant_id}/directions/", response_model=DirectionsResponse)
async def get_applicant_directions(applicant_id: int) -> JSONResponse:
    applicant = await applicant_service.get_applicant_with_directions(applicant_id)
    if applicant is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Applicant with ID {applicant_id} not found"
        )
    directions = applicant.directions
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "directions": [
                    DirectionSchema.from_orm(direction).dict()
                    for direction in directions
                ]
            }
        }
    )


@applicant_router.get(path="/schools/{school_id}/", response_model=ApplicantsResponse)
async def get_applicants_by_school_id(school_id: int) -> JSONResponse:
    applicants = await applicant_service.get_applicants_by_school_id(school_id)
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={
            "data": {
                "status": "ok",
                "applicants": [
                    ApplicantSchema.from_orm(applicant).dict()
                    for applicant in applicants
                ]
            }
        }
    )
