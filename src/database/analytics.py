from typing import List

from sqlalchemy import select, func

from src.database.context import DBContext
from src.database.models import School, Applicant, Direction

from src.analytics.schemas.schools import (
    TopSchool,
    TopSchoolByScore
)


class Analytics(DBContext):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def get_top_schools(
            self,
            top_n: int = 5
    ) -> List[TopSchool]:
        async with self.session() as session:
            stmt = (
                select(School.id, School.name, func.count(Applicant.school_id).label("count"))
                .join(Applicant, Applicant.school_id == School.id)
                .group_by(School.id, School.name)
                .order_by(func.count(Applicant.school_id).desc())
                .limit(top_n)
            )
            schools = await session.execute(stmt)
            return [
                TopSchool(id=id, name=name, count=count)
                for id, name, count in schools.all()
            ]

    async def get_top_schools_by_score(
            self,
            top_n: int = 5,
            count: int = 20,
    ) -> List[TopSchoolByScore]:
        async with self.session() as session:
            stmt = (
                select(
                    School.id,
                    School.name,
                    func.avg(Applicant.score).label("avg_score"),
                    func.count(Applicant.school_id).label("applicants_count")
                )
                .join(Applicant, Applicant.school_id == School.id)
                .group_by(School.id, School.name)
                .having(func.count(Applicant.school_id) > count)
                .order_by(func.avg(Applicant.score).desc())
                .limit(top_n)
            )
            schools = await session.execute(stmt)
            return [
                TopSchoolByScore(id=id, name=name, score=score, count=count)
                for id, name, score, count in schools.all()
            ]
