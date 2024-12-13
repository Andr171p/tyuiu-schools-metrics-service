from typing import List, Optional

from src.database.models.school import School
from src.database.models.applicant import Applicant
from src.database.services.school import school_service


class SchoolMetrics:
    _school: Optional[School] = None

    @classmethod
    async def get_school(cls, school_id: int) -> School | None:
        if cls._school is None:
            cls._school: School = await school_service.get_school_with_applicants(school_id)
        return cls._school

    @classmethod
    async def _get_applicants_count(cls) -> int:
        return len(cls._school.applicants)

    @classmethod
    async def _get_avg_gpa(cls) -> float:
        applicants: List[Applicant] = cls._school.applicants
        total_gpa: float = sum(applicant.gpa for applicant in applicants)
        avg_gpa: float = total_gpa / len(applicants) if len(applicants) > 0 else 0
        return round(avg_gpa, 3)

    @classmethod
    async def _get_avg_score(cls) -> float:
        applicants: List[Applicant] = cls._school.applicants
        total_score: int = sum(applicant.score for applicant in applicants)
        avg_score: float = total_score / len(applicants) if len(applicants) > 0 else 0
        return round(avg_score, 3)


s = SchoolMetrics()
import asyncio

async def main() -> None:
    await s.get_school(school_id=100)
    print(await s.get_applicants_count())
    print(await s.get_avg_gpa())
    print(await s.get_avg_score())


asyncio.run(main())