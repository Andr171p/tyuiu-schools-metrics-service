from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, relationship

from src.database.base import Base


if TYPE_CHECKING:
    from src.database.models.applicant import Applicant
    from src.database.models.metric import Metric


class School(Base):
    name: Mapped[str]
    city: Mapped[str]
    # latitude: Mapped[float]
    # longitude: Mapped[float]

    applicants: Mapped[list["Applicant"]] = relationship(back_populates="school")
    metric: Mapped["Metric"] = relationship(back_populates="school")

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.id}, name={self.name}"

    def __repr__(self) -> str:
        return str(self)
