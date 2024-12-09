from datetime import datetime

from sqlalchemy import DateTime, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import ARRAY

from src.database.base import Base


class Applicant(Base):
    full_name: Mapped[str]
    gender: Mapped[str]
    bdate: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    gpa: Mapped[float]
    score: Mapped[int]
    olympiads: Mapped[str | None] = mapped_column(nullable=True)
    university: Mapped[list[str]] = mapped_column(ARRAY(String))
    specialities: Mapped[list[str]] = mapped_column(ARRAY(String))
    reception: Mapped[str]
    order: Mapped[str | None] = mapped_column(nullable=True)

    school: Mapped
