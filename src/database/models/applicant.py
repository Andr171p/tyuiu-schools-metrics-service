from datetime import datetime
from typing import TYPE_CHECKING

from sqlalchemy import DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.database.base import Base
from src.database.models.mixins import SchoolRelationMixin


if TYPE_CHECKING:
    from src.database.models.personal import Personal


class Applicant(SchoolRelationMixin, Base):
    _school_back_populates = "applicants"

    full_name: Mapped[str]
    gender: Mapped[str]
    bdate: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    gpa: Mapped[float]
    score: Mapped[int]
    olympiads: Mapped[str | None] = mapped_column(nullable=True)

    personal: Mapped["Personal"] = relationship(back_populates="personal")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, full_name={self.full_name}, score={self.score}"

    def __repr__(self) -> str:
        return str(self)
