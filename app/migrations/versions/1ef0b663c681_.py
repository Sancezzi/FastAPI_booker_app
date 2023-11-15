"""empty message

Revision ID: 1ef0b663c681
Revises: 277c709c6e9e
Create Date: 2023-10-29 14:31:48.669937

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = '1ef0b663c681'
down_revision: Union[str, None] = '277c709c6e9e'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('rooms_quantity', sa.Integer(), nullable=False))
    op.drop_column('hotels', 'room_quantity')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('hotels', sa.Column('room_quantity', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_column('hotels', 'rooms_quantity')
    # ### end Alembic commands ###