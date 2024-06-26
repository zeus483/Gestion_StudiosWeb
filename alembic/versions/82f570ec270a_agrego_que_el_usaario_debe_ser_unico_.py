"""agrego que el usaario debe ser unico directo desde la base de datos

Revision ID: 82f570ec270a
Revises: c9de941cddcb
Create Date: 2024-05-11 21:34:59.127378

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '82f570ec270a'
down_revision: Union[str, None] = 'c9de941cddcb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    # Enable batch mode for SQLite compatibility
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint("uq_users_username", ['username'])
    # ### end Alembic commands ###

def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint("uq_users_username", type_='unique')
    # ### end Alembic commands ###