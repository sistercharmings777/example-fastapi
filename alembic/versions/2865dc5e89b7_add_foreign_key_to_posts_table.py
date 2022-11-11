"""add foreign-key to posts table

Revision ID: 2865dc5e89b7
Revises: f835f717ab0e
Create Date: 2022-11-09 16:14:12.155743

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2865dc5e89b7'
down_revision = 'f835f717ab0e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key("post_users_fk", source_table='posts', referent_table='users',
                          local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade() -> None:
    op.drop_constraint('post_users_fk', table_name='posts')
    op.drop_column('posts', 'owner_id')
    pass
