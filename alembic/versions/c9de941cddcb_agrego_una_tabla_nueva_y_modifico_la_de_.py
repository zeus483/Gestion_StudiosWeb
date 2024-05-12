"""agrego una tabla nueva y modifico la de modelos

Revision ID: c9de941cddcb
Revises: b9e7962837d6
Create Date: 2024-05-11 19:04:37.678613

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c9de941cddcb'
down_revision: Union[str, None] = 'b9e7962837d6'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('financial_records',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('model_id', sa.Integer(), nullable=True),
    sa.Column('tokens', sa.Integer(), nullable=True),
    sa.Column('usd_amount', sa.Float(), nullable=True),
    sa.Column('local_currency_amount', sa.Float(), nullable=True),
    sa.Column('exchange_rate', sa.Float(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['model_id'], ['models.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('models', sa.Column('tokens_generated', sa.Integer(), nullable=True))
    op.add_column('models', sa.Column('connection_hours', sa.Float(), nullable=True))
    op.add_column('models', sa.Column('token_goal', sa.Integer(), nullable=True))
    op.add_column('models', sa.Column('rest_days', sa.Date(), nullable=True))
    op.add_column('models', sa.Column('follower_growth', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('models', 'follower_growth')
    op.drop_column('models', 'rest_days')
    op.drop_column('models', 'token_goal')
    op.drop_column('models', 'connection_hours')
    op.drop_column('models', 'tokens_generated')
    op.drop_table('financial_records')
    # ### end Alembic commands ###
