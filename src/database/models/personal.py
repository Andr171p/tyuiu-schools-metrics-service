from sqlalchemy.orm import Mapped, mapped_column

from src.database.base import Base
from src.database.models.mixins import ApplicantRelationMixin


class Personal(ApplicantRelationMixin, Base):
    _applicant_id_unique = True
    _applicant_back_populates = "personal"

    phone: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str] = mapped_column(nullable=True)
