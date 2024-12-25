from fastapi import APIRouter, status
from fastapi.responses import JSONResponse
# from fastapi.exceptions import HTTPException

from src.config import settings
from src.database.services.applicant import applicant_service
from src.api_v1.schemas.applicant import ApplicantSchema, ApplicantsResponse


applicant_router = APIRouter(
    prefix=f"{settings.api.api_v1_prefix}/applicants",
    tags=["Applicants"]
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
