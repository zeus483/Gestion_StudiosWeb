"""hago que el campo username de la tabla model sea unico, es decir no puedan haber 2 username iguales

Revision ID: 9aefab6065c3
Revises: ddad7627ec0b
Create Date: 2024-05-13 15:35:41.423815

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9aefab6065c3'
down_revision: Union[str, None] = 'ddad7627ec0b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Usar `batch_alter_table` para operaciones que requieren reconstrucción de la tabla
    with op.batch_alter_table('models', schema=None) as batch_op:
        batch_op.create_unique_constraint('uq_models_username', ['username'])

def downgrade():
    with op.batch_alter_table('models', schema=None) as batch_op:
        batch_op.drop_constraint('uq_models_username', type_='unique')  