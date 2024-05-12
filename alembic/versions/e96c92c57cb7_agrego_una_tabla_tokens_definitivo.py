"""agrego una tabla tokens definitivo

Revision ID: e96c92c57cb7
Revises: c754eaf0055f
Create Date: 2024-05-12 10:31:15.847494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e96c92c57cb7'
down_revision: Union[str, None] = 'c754eaf0055f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tokens',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('name_page', sa.String(), nullable=True),
    sa.Column('tokens', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['name_page'], ['pages.name'], ),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tokens')
    # ### end Alembic commands ###
