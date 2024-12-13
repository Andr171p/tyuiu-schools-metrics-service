from typing import List

from src.database.context import DBContext
from src.database.models.direction import Direction


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