from typing import Sequence, List, Optional

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

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

    async def get_applicant(self, id: int) -> Applicant | None:
        async with self.session() as session:
            stmt = (
                select(Applicant)
                .where(Applicant.id == id)
            )
            applicant = await session.execute(stmt)
            return applicant.scalar_one_or_none()

    async def get_applicants_by_school_id(
            self,
            school_id: int
    ) -> Sequence[Applicant]:
        async with self.session() as session:
            stmt = (
                select(Applicant)
                .where(Applicant.school_id == school_id)
            )
            applicants = await session.execute(stmt)
            return applicants.scalars().all()

    async def get_applicant_by_full_name(
            self,
            full_name: str
    ) -> Applicant | None:
        async with self.session() as session:
            stmt = (
                select(Applicant)
                .options(joinedload(Applicant.school))
                .where(Applicant.full_name == full_name)
            )
            applicant = await session.execute(stmt)
            return applicant.scalar_one_or_none()

    async def get_applicant_with_directions(self, id: int) -> Applicant:
        async with self.session() as session:
            stmt = (
                select(Applicant)
                .options(selectinload(Applicant.directions))
                .where(Applicant.id == id)
            )
            applicant = await session.execute(stmt)
            return applicant.scalar_one_or_none()


applicant_service = ApplicantService()
