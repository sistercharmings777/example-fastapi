""" add last few columns to post table

Revision ID: 0e600345ed02
Revises: 2865dc5e89b7
Create Date: 2022-11-09 16:27:28.166202

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e600345ed02'
down_revision = '2865dc5e89b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('published', sa.Boolean(),
                  nullable=False, server_default="True"))
    op.add_column('posts', sa.Column('created_at', sa.TIMESTAMP(
        timezone=True), nullable=False, server_default=sa.text('NOW()')))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'published')
    op.drop_column("posts", "created_at")
    pass
