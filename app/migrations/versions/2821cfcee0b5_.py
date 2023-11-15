"""empty message

Revision ID: 2821cfcee0b5
Revises: caba544c51a3
Create Date: 2023-10-29 14:09:28.903812

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '2821cfcee0b5'
down_revision: Union[str, None] = 'caba544c51a3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
