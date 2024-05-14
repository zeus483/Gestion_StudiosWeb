"""cambio las relaciones de tokens, para que se relaciones es con una cuenta, no con las paginas

Revision ID: 6590c30ef2e7
Revises: 9aefab6065c3
Create Date: 2024-05-14 18:31:25.128070

"""
from typing import Sequence, Union
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6590c30ef2e7'
down_revision: Union[str, None] = '9aefab6065c3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Crear nueva tabla tokens con la clave foránea actualizada
    op.create_table(
        'tokens_new',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String, sa.ForeignKey('users.username')),
        sa.Column('name_page', sa.String, sa.ForeignKey('accounts.page')),
        sa.Column('tokens', sa.Integer, default=0),
    )

    # Copiar los datos de la tabla antigua a la nueva
    op.execute('''
        INSERT INTO tokens_new (id, username, name_page, tokens)
        SELECT id, username, name_page, tokens FROM tokens
    ''')

    # Eliminar la tabla antigua
    op.drop_table('tokens')

    # Renombrar la nueva tabla a tokens
    op.rename_table('tokens_new', 'tokens')


def downgrade() -> None:
    # Crear la tabla tokens antigua
    op.create_table(
        'tokens_old',
        sa.Column('id', sa.Integer, primary_key=True, autoincrement=True),
        sa.Column('username', sa.String, sa.ForeignKey('users.username')),
        sa.Column('name_page', sa.String, sa.ForeignKey('pages.name')),
        sa.Column('tokens', sa.Integer, default=0),
    )

    # Copiar los datos de la tabla nueva a la antigua
    op.execute('''
        INSERT INTO tokens_old (id, username, name_page, tokens)
        SELECT id, username, name_page, tokens FROM tokens
    ''')

    # Eliminar la tabla nueva
    op.drop_table('tokens')

    # Renombrar la tabla antigua a tokens
    op.rename_table('tokens_old', 'tokens')
