"""ultimos cambios

Revision ID: ed8d2bb160e6
Revises: 75b223e9ad27
Create Date: 2024-05-09 15:31:26.448122

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = 'ed8d2bb160e6'
down_revision = '75b223e9ad27'
branch_labels = None
depends_on = None

def upgrade():
    # Contexto de binding necesario para el modo batch
    bind = op.get_bind()
    if bind.dialect.name == 'sqlite':
        # Usar modo batch para SQLite
        with op.batch_alter_table('accounts', schema=None) as batch_op:
            batch_op.add_column(sa.Column('user_model', sa.String(), nullable=True))
            batch_op.create_foreign_key(
                'fk_accounts_users', 'users', ['user_model'], ['username']
            )
    else:
        # Para otros SGBD que soportan ALTER directo
        op.add_column('accounts', sa.Column('user_model', sa.String(), nullable=True))
        op.create_foreign_key(None, 'accounts', 'users', ['user_model'], ['username'])

def downgrade():
    bind = op.get_bind()
    if bind.dialect.name == 'sqlite':
        with op.batch_alter_table('accounts', schema=None) as batch_op:
            batch_op.drop_constraint('fk_accounts_users', type_='foreignkey')
            batch_op.drop_column('user_model')
    else:
        op.drop_constraint(None, 'accounts', type_='foreignkey')
        op.drop_column('accounts', 'user_model')
