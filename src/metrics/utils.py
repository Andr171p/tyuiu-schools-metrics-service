from typing import List, Sequence
from collections import Counter

from src.database.models.applicant import Applicant
from src.database.models.direction import Direction


def get_applicants_count(applicants: Sequence[Applicant]) -> int:
    return len(applicants)


def get_students_count(directions: Sequence[Direction]) -> int:
    count: int = 0
    for direction in directions:
        if direction.order is not None:
            count += 1
    return count


def get_avg_gpa(applicants: Sequence[Applicant]) -> float:
    total_gpa: float = sum(applicant.gpa for applicant in applicants)
    avg_gpa: float = total_gpa / len(applicants) if len(applicants) > 0 else 0
    return round(avg_gpa, 3)


def get_avg_score(applicants: Sequence[Applicant]) -> float:
    total_gpa: float = sum(applicant.gpa for applicant in applicants)
    avg_gpa: float = total_gpa / len(applicants) if len(applicants) > 0 else 0
    return round(avg_gpa, 3)


def get_popular_universities(
        directions: Sequence[Direction],
        top_n: int = 5
) -> List[str]:
    universities_list: List[str] = [direction.university for direction in directions]
    counter = Counter(universities_list)
    return [university for university, _ in counter.most_common(top_n)]


def get_popular_directions(
        directions: Sequence[Direction],
        top_n: int = 5
) -> List[str]:
    directions_list: List[str] = [direction.direction for direction in directions]
    counter = Counter(directions_list)
    return [direction for direction, _ in counter.most_common(top_n)]
