from typing import Sequence, Dict, List

from sqlalchemy import select, func

from src.database.context import DBContext
from src.database.models import School, Applicant, Direction


class DirectionMetrics(DBContext):
    def __init__(self) -> None:
        super().__init__()
        self.init()
        ...

    async def get_top_schools_by_university(
            self,
            university: str,
            top_n: int = 3
    ) -> Sequence[School] | None:
        async with self.session() as session:
            stmt = (
                select(School.name, func.count(Applicant.id).label("count"))
                .join(Applicant.directions)
                .filter(Direction.university == university)
                .group_by(School.name)
                .order_by(func.count(Applicant.id).desc())
                .limit(top_n)
            )
            try:
                schools = await session.execute(stmt)
                return schools.scalars().all()
            except Exception as _ex:
                raise _ex

    async def get_top_universities(self, top_n: int = 3) -> ...:
        async with self.session() as session:
            stmt = (
                select(School.name.label("school"), Direction.university.label("university"))
                .join(School.applicants)
                .join(Applicant.directions)
                .group_by(School.name, Direction.university)
                .order_by(func.count().desc(), School.name)
                .limit(top_n)
            )
            universities = await session.execute(stmt)
            rows = universities.all()
            universities_dict: Dict[str, List[str]] = {}
            for school, university in rows:
                if university not in universities_dict:
                    universities_dict[university] = []
                universities_dict[university].append(school)

            return universities_dict


import asyncio
print(asyncio.run(DirectionMetrics().get_top_universities()))
