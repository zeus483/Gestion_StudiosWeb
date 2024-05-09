"""Merge multiple heads

Revision ID: 75b223e9ad27
Revises: d860410ac328, e8278678ed49
Create Date: 2024-05-09 15:29:25.906268

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '75b223e9ad27'
down_revision: Union[str, None] = ('d860410ac328', 'e8278678ed49')
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
