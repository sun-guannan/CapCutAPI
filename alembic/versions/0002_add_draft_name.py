"""add draft_name column to drafts

Revision ID: 0002_add_draft_name
Revises: 0001_initial
Create Date: 2025-09-17 00:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0002_add_draft_name'
down_revision = '0001_initial'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('drafts', sa.Column('draft_name', sa.String(length=255), nullable=True))


def downgrade() -> None:
    op.drop_column('drafts', 'draft_name')


