"""add column to posts table

Revision ID: 5291b86316f3
Revises: ef7474875fac
Create Date: 2024-01-27 22:00:27.216831

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5291b86316f3'
down_revision: Union[str, None] = 'ef7474875fac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
