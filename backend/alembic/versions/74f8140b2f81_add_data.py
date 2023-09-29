"""add_data

Revision ID: 74f8140b2f81
Revises: f5f36a39bb61
Create Date: 2023-09-28 18:41:09.836682

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '74f8140b2f81'
down_revision: Union[str, None] = 'f5f36a39bb61'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass

def downgrade() -> None:
    pass
