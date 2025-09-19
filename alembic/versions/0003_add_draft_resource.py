"""add resource column to drafts

Revision ID: 0003_add_draft_resource
Revises: 0002_add_draft_name
Create Date: 2025-09-19 00:00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0003_add_draft_resource'
down_revision = '0002_add_draft_name'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # Create enum type if not exists and add column
    draft_resource = sa.Enum('api', 'mcp', name='draft_resource')
    draft_resource.create(op.get_bind(), checkfirst=True)
    op.add_column('drafts', sa.Column('resource', draft_resource, nullable=True))


def downgrade() -> None:
    op.drop_column('drafts', 'resource')
    # Drop enum type
    sa.Enum(name='draft_resource').drop(op.get_bind(), checkfirst=True)


