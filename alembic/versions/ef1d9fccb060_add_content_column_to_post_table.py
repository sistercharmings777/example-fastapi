"""add content column to post table

Revision ID: ef1d9fccb060
Revises: dbeb197f8bde
Create Date: 2022-11-09 15:33:31.446089

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ef1d9fccb060'
down_revision = 'dbeb197f8bde'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
