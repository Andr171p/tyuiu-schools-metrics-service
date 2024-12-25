from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base
from src.database.models.mixins import ApplicantRelationMixin


class Direction(ApplicantRelationMixin, Base):
    _applicant_back_populates = "directions"

    university: Mapped[str]
    reception: Mapped[str]
    direction: Mapped[str]
    order: Mapped[str | None] = mapped_column(nullable=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(university={self.university}, reception={self.reception}, direction={self.direction}, order={self.order})"

    def __repr__(self) -> str:
        return str(self)
