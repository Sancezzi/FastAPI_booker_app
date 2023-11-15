"""empty message

Revision ID: bfdc3ed7b835
Revises: 2821cfcee0b5
Create Date: 2023-10-29 14:26:31.073042

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'bfdc3ed7b835'
down_revision: Union[str, None] = '2821cfcee0b5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
