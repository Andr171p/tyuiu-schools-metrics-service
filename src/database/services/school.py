from typing import Any, Sequence, List
from functools import singledispatchmethod

from sqlalchemy import select
from sqlalchemy.orm import joinedload, selectinload

from src.database.context import DBContext
from src.database.models.school import School


class SchoolService(DBContext):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def add_school(self, school: School) -> School:
        async with self.session() as session:
            session.add(school)
            await session.commit()
            return school

    async def add_schools(self, schools: List[School]) -> List[School]:
        async with self.session() as session:
            session.add_all(schools)
            await session.commit()
            return schools

    async def get_schools(self) -> Sequence[School] | None:
        async with self.session() as session:
            stmt = select(School)
            schools = await session.execute(stmt)
            return schools.scalars().all()

    @singledispatchmethod
    async def get_school(self, arg: Any) -> School | None:
        raise NotImplementedError("<SchoolService> get_school not implemented")

    @get_school.register
    async def _(self, id: int) -> School | None:
        async with self.session() as session:
            stmt = select(School).where(School.id == id)
            school = await session.execute(stmt)
            return school.scalar_one_or_none()

    @get_school.register
    async def _(self, name: str) -> School | None:
        async with self.session() as session:
            stmt = select(School).where(School.name == name)
            school = await session.execute(stmt)
            return school.scalar_one_or_none()

    async def get_schools_by_city(self, city: str) -> Sequence[School] | None:
        async with self.session() as session:
            stmt = select(School).where(School.city == city)
            schools = await session.execute(stmt)
            return schools.scalars().all()

    async def get_schools_with_applicants(self) -> Sequence[School] | None:
        async with self.session() as session:
            stmt = (
                select(School)
                .options(
                    selectinload(School.applicants),
                ).order_by(School.id)
            )
            schools = await session.execute(stmt)
            return schools.scalars().all()

    async def get_school_with_applicants(self, id: int) -> School | None:
        async with self.session() as session:
            stmt = (
                select(School)
                .where(School.id == id)
                .options(
                    selectinload(School.applicants)
                ).order_by(School.id)
            )
            school = await session.execute(stmt)
            return school.scalars().one()


school_service = SchoolService()


import asyncio
print(asyncio.run(school_service.get_schools()))
