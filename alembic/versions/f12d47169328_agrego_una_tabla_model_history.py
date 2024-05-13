"""agrego una tabla model_history

Revision ID: f12d47169328
Revises: e96c92c57cb7
Create Date: 2024-05-12 11:06:18.435387

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f12d47169328'
down_revision: Union[str, None] = 'e96c92c57cb7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('model_history',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.Column('tokens_generated', sa.Integer(), nullable=True),
    sa.Column('token_goal', sa.Integer(), nullable=True),
    sa.Column('period_end_date', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['model_id'], ['models.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('model_history')
    # ### end Alembic commands ###