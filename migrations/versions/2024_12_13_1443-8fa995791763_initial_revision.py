"""Initial revision

Revision ID: 8fa995791763
Revises: 
Create Date: 2024-12-13 14:43:41.587521

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8fa995791763'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('schools',
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('applicants',
    sa.Column('full_name', sa.String(), nullable=False),
    sa.Column('gender', sa.String(), nullable=False),
    sa.Column('bdate', sa.DateTime(), nullable=False),
    sa.Column('gpa', sa.Float(), nullable=False),
    sa.Column('score', sa.Integer(), nullable=False),
    sa.Column('olympiads', sa.String(), nullable=True),
    sa.Column('school_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['school_id'], ['schools.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('metrics',
    sa.Column('applicants', sa.Integer(), nullable=False),
    sa.Column('students', sa.Integer(), nullable=False),
    sa.Column('gpa', sa.Float(), nullable=False),
    sa.Column('score', sa.Float(), nullable=False),
    sa.Column('school_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['school_id'], ['schools.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('school_id')
    )
    op.create_table('directions',
    sa.Column('university', sa.String(), nullable=False),
    sa.Column('reception', sa.String(), nullable=False),
    sa.Column('direction', sa.String(), nullable=False),
    sa.Column('order', sa.String(), nullable=True),
    sa.Column('applicant_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['applicant_id'], ['applicants.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('personals',
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('applicant_id', sa.Integer(), nullable=False),
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['applicant_id'], ['applicants.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('applicant_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('personals')
    op.drop_table('directions')
    op.drop_table('metrics')
    op.drop_table('applicants')
    op.drop_table('schools')
    # ### end Alembic commands ###