"""add soft delete flag to drafts

Revision ID: 0005_add_draft_soft_delete
Revises: 0004_make_datetime_tz_aware
Create Date: 2025-09-22 00:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0005_add_draft_soft_delete'
down_revision = '0004_make_datetime_tz_aware'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('drafts', sa.Column('is_deleted', sa.Boolean(), nullable=False, server_default=sa.false()))
    # Ensure default is False for existing rows, then drop server_default
    op.create_index('ix_drafts_is_deleted', 'drafts', ['is_deleted'])
    op.alter_column('drafts', 'is_deleted', server_default=None)


def downgrade() -> None:
    op.drop_index('ix_drafts_is_deleted', table_name='drafts')
    op.drop_column('drafts', 'is_deleted')


