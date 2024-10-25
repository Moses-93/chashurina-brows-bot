"""add_new_field user_id

Revision ID: 1e4c453220b7
Revises: 
Create Date: 2024-10-15 19:12:09.479649

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "1e4c453220b7"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("main_notes", sa.Column("user_id", sa.Integer(), nullable=True))
    op.create_index(
        op.f("ix_main_notes_user_id"), "main_notes", ["user_id"], unique=True
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_main_notes_user_id"), table_name="main_notes")
    op.drop_column("main_notes", "user_id")
    # ### end Alembic commands ###