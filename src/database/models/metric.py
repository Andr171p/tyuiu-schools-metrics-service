from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base


class Metric(Base):
    applicants: Mapped[int]
    students: Mapped[int]
    gpa: Mapped[float]
    score: Mapped[float]
    ...
