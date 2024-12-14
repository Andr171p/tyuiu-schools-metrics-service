from typing import List, Sequence

from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.database.context import DBContext
from src.database.models.direction import Direction
from src.database.models.applicant import Applicant
from src.database.models.school import School


class DirectionService(DBContext):
    def __init__(self) -> None:
        super().__init__()
        self.init()

    async def add_directions(
            self,
            directions: List[Direction]
    ) -> List[Direction]:
        async with self.session() as session:
            session.add_all(directions)
            await session.commit()
            return directions

    async def get_directions_by_school_id(
            self,
            school_id: int
    ) -> Sequence[Direction]:
        async with self.session() as session:
            stmt = (
                select(Direction)
                .join(Direction.applicant)
                .join(Applicant.school)
                .where(School.id == school_id)
                .options(joinedload(Direction.applicant))
            )
            directions = await session.execute(stmt)
            return directions.scalars().all()


direction_service = DirectionService()
