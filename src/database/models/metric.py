from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base
from src.database.models.mixins import SchoolRelationMixin


class Metric(SchoolRelationMixin, Base):
    _school_id_unique = True
    _school_back_populates = "metric"

    applicants: Mapped[int]
    students: Mapped[int]
    gpa: Mapped[float]
    score: Mapped[float]
