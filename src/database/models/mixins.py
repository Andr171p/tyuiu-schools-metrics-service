from sqlalchemy import ForeignKey
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    declared_attr,
    relationship
)

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from src.database.models.school import School
    from src.database.models.applicant import Applicant


class SchoolRelationMixin:
    _school_id_nullable: bool = False
    _school_id_unique: bool = False
    _school_back_populates: str | None = None

    @declared_attr
    def school_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("schools.id"),
            unique=cls._school_id_unique,
            nullable=cls._school_id_nullable
        )

    @declared_attr
    def school(cls) -> Mapped["School"]:
        return relationship(
            argument="School",
            back_populates=cls._school_back_populates
        )


class ApplicantRelationMixin:
    _applicant_id_unique: bool = False
    _applicant_id_nullable: bool = False
    _applicant_back_populates: str | None = None

    @declared_attr
    def applicant_id(cls) -> Mapped[int]:
        return mapped_column(
            ForeignKey("applicants.id"),
            unique=cls._applicant_id_unique,
            nullable=cls._applicant_id_nullable
        )

    @declared_attr
    def applicant(cls) -> Mapped["Applicant"]:
        return relationship(
            argument="Applicant",
            back_populates=cls._applicant_back_populates
        )
