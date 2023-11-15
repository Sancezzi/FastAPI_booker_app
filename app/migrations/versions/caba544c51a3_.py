"""empty message

Revision ID: caba544c51a3
Revises: 98c334a21bdb
Create Date: 2023-10-29 14:08:09.639166

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = 'caba544c51a3'
down_revision: Union[str, None] = '98c334a21bdb'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
