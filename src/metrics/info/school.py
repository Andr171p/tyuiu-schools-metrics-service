from typing import List, Optional, Sequence
from dataclasses import dataclass

from src.database.models.applicant import Applicant
from src.database.models.direction import Direction
from src.database.services.applicant import ApplicantService
from src.database.services.direction import DirectionService

from src.metrics import utils


@dataclass
class Metric:
    applicants_count: int
    students_count: int
    avg_gpa: float
    avg_score: float
    popular_universities: List[str]
    popular_directions: List[str]


class SchoolInfoMetric(ApplicantService, DirectionService):
    _applicants: Optional[Sequence[Applicant]] = None
    _directions: Optional[Sequence[Direction]] = None

    def __init__(self, school_id: int) -> None:
        super().__init__()
        self._school_id = school_id
        self.metric: Optional[type[Metric]] = Metric

    async def _get_school_data(self) -> None:
        self._applicants = await self.get_applicants_by_school_id(self._school_id)
        self._directions = await self.get_directions_by_school_id(self._school_id)

    @staticmethod
    def _check_count(
            applicants: Sequence[Applicant],
            count: int = 20
    ) -> bool:
        return True if len(applicants) > count else False

    async def get_school_metrics(self) -> Metric | None:
        await self._get_school_data()
        if not self._check_count(self._applicants):
            return
        self.metric.applicants_count = utils.get_applicants_count(self._applicants)
        self.metric.students_count = utils.get_students_count(self._directions)
        self.metric.avg_gpa = utils.get_avg_gpa(self._applicants)
        self.metric.avg_score = utils.get_avg_score(self._applicants)
        self.metric.popular_universities = utils.get_popular_universities(self._directions)
        self.metric.popular_directions = utils.get_popular_directions(self._directions)
        return self.metric
