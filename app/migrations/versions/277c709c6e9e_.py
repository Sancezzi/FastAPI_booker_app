"""empty message

Revision ID: 277c709c6e9e
Revises: bfdc3ed7b835
Create Date: 2023-10-29 14:28:52.334352

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '277c709c6e9e'
down_revision: Union[str, None] = 'bfdc3ed7b835'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
