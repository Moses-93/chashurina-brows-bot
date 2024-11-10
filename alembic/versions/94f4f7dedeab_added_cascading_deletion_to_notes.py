"""added cascading deletion to Notes

Revision ID: 94f4f7dedeab
Revises: 9b9e2ce0b01e
Create Date: 2024-11-10 15:48:14.979346

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "94f4f7dedeab"
down_revision: Union[str, None] = "9b9e2ce0b01e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint("main_notes_date_id_fkey", "main_notes", type_="foreignkey")
    op.drop_constraint("main_notes_service_id_fkey", "main_notes", type_="foreignkey")
    op.create_foreign_key(
        None, "main_notes", "main_service", ["service_id"], ["id"], ondelete="CASCADE"
    )
    op.create_foreign_key(
        None, "main_notes", "main_freedate", ["date_id"], ["id"], ondelete="CASCADE"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "main_notes", type_="foreignkey")
    op.drop_constraint(None, "main_notes", type_="foreignkey")
    op.create_foreign_key(
        "main_notes_service_id_fkey",
        "main_notes",
        "main_service",
        ["service_id"],
        ["id"],
    )
    op.create_foreign_key(
        "main_notes_date_id_fkey", "main_notes", "main_freedate", ["date_id"], ["id"]
    )
    # ### end Alembic commands ###
