from typing import Optional, List, Dict, Any

from sqlalchemy import select
from sqlalchemy import text

from src.database.context import DBContext
from src.database.models.school import School
from src.database.models.applicant import Applicant


class ApplicantService(DBContext):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def add_applicant_by_school_id(
            self,
            school_id: int,
            applicant: Applicant
    ) -> Optional[Applicant]:
        async with self.session() as session:
            stmt = (
                select(School)
                .where(School.id == school_id)
            )
            school = await session.execute(stmt)
            school = school.scalar_one_or_none()
            if school is None:
                raise ValueError(f"<School> with id: {school_id} not found")
            applicant.school_id = school_id
            session.add(applicant)
            await session.flush()
        return applicant

    async def add_applicants(
            self,
            applicants: List[Applicant]
    ) -> List[Applicant]:
        async with self.session() as session:
            session.add_all(applicants)
            await session.commit()
            return applicants

    async def truncate_applicants(self) -> None:
        async with self.session() as session:
            await session.execute(text("TRUNCATE TABLE applicants CASCADE   "))
            await session.commit()
