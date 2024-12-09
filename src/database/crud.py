from sqlalchemy import select, insert, update, delete
from typing import Generic, List, Optional

from src.database.context import DBContext
from src.database.base import ModelType


class CRUD(DBContext, Generic[ModelType]):
    def __init__(self, model: type[ModelType]) -> None:
        super().__init__()
        self.init()
        self._model = model

    async def create(self, model: ModelType) -> ModelType | None:
        async with (self.session() as session):
            stmt = insert(self._model).values(**model.__dict__).returning(self._model)
            db_model = await session.execute(stmt)
            db_model = db_model.fetchone()
            await session.flush()
            return db_model

    async def read(self, id: int) -> ModelType:
        async with self.session() as session:
            stmt = select(self._model).where(self._model.id == id)
            model = await session.execute(stmt)
            return model.scalar_one_or_none()

    async def read_all(
            self,
            offset: int = 0,
            limit: int = 100
    ) -> List[ModelType]:
        ...

    async def update(
            self,
            id: int,
            model: ModelType
    ) -> Optional[ModelType]:
        async with self.session() as session:
            stmt = (
                update(self._model)
                .where(self._model.id == id)
                .values(**model.dict(exclude_unset=True))
                .returning(self._model)
            )
            model = await session.execute(stmt)
            return model.scalar_one_or_none()

    async def delete(self, id: int) -> bool:
        async with self.session() as session:
            stmt = delete(self._model).where(self._model.id == id)
            exists = await session.execute(stmt)
            await session.commit()
            return exists.rowcount() > 0
