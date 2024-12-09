__all__ = (
    "Base",
    "School",
    "Profile",
    "Applicant",
    "Speciality"
)

from src.database.base import Base
from src.database.models.school import School
from src.database.models.metric import Profile
from src.database.models.applicant import Applicant
from src.database.models.direction import Speciality