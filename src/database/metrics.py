from typing import Sequence, List, Tuple

from sqlalchemy import select
from sqlalchemy.sql.expression import func

from src.database.context import DBContext
from src.database.models.applicant import Applicant
from src.database.models.direction import Direction


class SchoolMetrics(DBContext):
    def __init__(self, school_id: int) -> None:
        super().__init__()
        self.init()
        self._id = school_id

    async def get_applicants_count(self) -> int:
        async with self.session() as session:
            stmt = (
                select(func.count())
                .select_from(Applicant)
                .where(Applicant.school_id == self._id)
            )
            count = await session.execute(stmt)
            return count.scalar()

    async def get_students_count(self) -> int:
        async with self.session() as session:
            stmt = (
                select(func.count())
                .select_from(Applicant)
                .join(Applicant.directions)
                .where(Applicant.school_id == self._id)
                .where(Direction.order != None)
            )
            count = await session.execute(stmt)
            return count.scalar()

    async def get_avg_gpa(self) -> float:
        async with self.session() as session:
            stmt = (
                select(func.avg(Applicant.gpa))
                .select_from(Applicant)
                .where(Applicant.school_id == self._id)
            )
            avg_gpa = await session.execute(stmt)
            return round(avg_gpa.scalar(), 3) or 0.0

    async def get_avg_score(self) -> float:
        async with self.session() as session:
            stmt = (
                select(func.avg(Applicant.score))
                .select_from(Applicant)
                .where(Applicant.school_id == self._id)
            )
            avg_score = await session.execute(stmt)
            return round(avg_score.scalar(), 3) or 0.0

    async def get_top_directions(
            self,
            top_n: int = 3
    ) -> List[Tuple[str, int]]:
        async with self.session() as session:
            stmt = (
                select(Direction.direction, func.count())
                .select_from(Direction)
                .join(Direction.applicant)
                .where(Applicant.school_id == self._id)
                .group_by(Direction.direction)
                .order_by(func.count().desc())
                .limit(top_n)
            )
            distribution = await session.execute(stmt)
            return [
                (item.direction, item.count)
                for item in distribution.all()
            ]

    async def get_top_universities(
            self,
            top_n: int = 3
    ) -> List[Tuple[str, int]]:
        async with self.session() as session:
            stmt = (
                select(Direction.university, func.count())
                .select_from(Direction)
                .join(Direction.applicant)
                .where(Applicant.school_id == self._id)
                .group_by(Direction.university)
                .order_by(func.count().desc())
                .limit(top_n)
            )
            distribution = await session.execute(stmt)
            return [
                (item.university, item.count)
                for item in distribution.all()
            ]

    async def get_olympiads_count(self) -> int:
        async with self.session() as session:
            stmt = (
                select(func.count())
                .select_from(Applicant)
                .where(Applicant.school_id == self._id)
                .where(Applicant.olympiads.isnot(None))
            )
            count = await session.execute(stmt)
            return count.scalar()

    async def get_genders_count(self) -> List[Tuple[str, int]]:
        async with self.session() as session:
            stmt = (
                select(Applicant.gender, func.count())
                .select_from(Applicant)
                .where(Applicant.school_id == self._id)
                .group_by(Applicant.gender)
            )
            distribution = await session.execute(stmt)
            return [
                (item.gender, item.count)
                for item in distribution.all()
            ]


import inspect

print(inspect.getmembers(SchoolMetrics, predicate=inspect.isfunction))
