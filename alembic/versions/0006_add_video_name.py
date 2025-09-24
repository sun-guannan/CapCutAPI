"""add video_name to video_tasks

Revision ID: 0006_add_video_name
Revises: 0005_add_draft_soft_delete
Create Date: 2025-09-23 00:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0006_add_video_name'
down_revision = '0005_add_draft_soft_delete'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('video_tasks', sa.Column('video_name', sa.String(length=255), nullable=True))


def downgrade() -> None:
    op.drop_column('video_tasks', 'video_name')



