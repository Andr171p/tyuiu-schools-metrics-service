__all__ = (
    "Base",
    "School",
    "Metric",
    "Applicant",
    "Direction",
    "Personal"
)

from src.database.base import Base
from src.database.models.school import School
from src.database.models.metric import Metric
from src.database.models.applicant import Applicant
from src.database.models.direction import Direction
from src.database.models.personal import Personal