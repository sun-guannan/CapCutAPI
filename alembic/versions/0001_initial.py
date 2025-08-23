"""initial tables

Revision ID: 0001_initial
Revises: 
Create Date: 2025-08-22 00:00:00

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision = '0001_initial'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        'drafts',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('draft_id', sa.String(length=255), nullable=False),
        sa.Column('data', sa.LargeBinary(), nullable=False),
        sa.Column('width', sa.Integer(), nullable=True),
        sa.Column('height', sa.Integer(), nullable=True),
        sa.Column('duration', sa.Integer(), nullable=True),
        sa.Column('fps', sa.Float(), nullable=True),
        sa.Column('version', sa.String(length=64), nullable=True),
        sa.Column('size_bytes', sa.Integer(), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
        sa.Column('accessed_at', sa.DateTime(), nullable=True),
    )
    op.create_index('ix_drafts_draft_id', 'drafts', ['draft_id'], unique=True)

    op.create_table(
        'video_tasks',
        sa.Column('id', sa.Integer(), primary_key=True, autoincrement=True),
        sa.Column('task_id', sa.String(length=255), nullable=False),
        sa.Column('draft_id', sa.String(length=255), nullable=False),
        sa.Column('status', sa.String(length=64), nullable=False),
        sa.Column('progress', sa.Integer(), nullable=True),
        sa.Column('message', sa.Text(), nullable=True),
        sa.Column('draft_url', sa.Text(), nullable=True),
        sa.Column('extra', postgresql.JSONB(astext_type=sa.Text()), nullable=True),
        sa.Column('created_at', sa.DateTime(), nullable=False),
        sa.Column('updated_at', sa.DateTime(), nullable=False),
    )
    op.create_index('ix_video_tasks_task_id', 'video_tasks', ['task_id'], unique=True)
    op.create_index('ix_video_tasks_draft_id', 'video_tasks', ['draft_id'], unique=False)
    op.create_index('ix_video_tasks_status', 'video_tasks', ['status'], unique=False)


def downgrade() -> None:
    op.drop_index('ix_video_tasks_status', table_name='video_tasks')
    op.drop_index('ix_video_tasks_draft_id', table_name='video_tasks')
    op.drop_index('ix_video_tasks_task_id', table_name='video_tasks')
    op.drop_table('video_tasks')

    op.drop_index('ix_drafts_draft_id', table_name='drafts')
    op.drop_table('drafts')


