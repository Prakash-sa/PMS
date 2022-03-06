from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

revision = "20251005_0001"
down_revision = None
branch_labels = None
depends_on = None

def upgrade() -> None:
    op.execute("CREATE EXTENSION IF NOT EXISTS postgis;")
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("sub", sa.String, unique=True, index=True),
        sa.Column("email", sa.String, unique=True, index=True),
        sa.Column("role", sa.Enum("admin","reviewer","submitter", name="roleenum"), nullable=False),
        sa.Column("is_active", sa.Boolean, server_default=sa.text("true")),
    )
    op.create_table(
        "proposals",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String, nullable=False),
        sa.Column("pest_type", sa.String, nullable=False),
        sa.Column("chemical", sa.String, nullable=False),
        sa.Column("rate", sa.String),
        sa.Column("method", sa.String),
        sa.Column("created_by_id", sa.Integer, sa.ForeignKey("users.id"))
    )
    op.execute("ALTER TABLE proposals ADD COLUMN geometry geometry(MULTIPOLYGON, 4326);")
    op.create_table(
        "approvals",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("proposal_id", sa.Integer, sa.ForeignKey("proposals.id", ondelete="CASCADE")),
        sa.Column("status", sa.Enum("pending","approved","rejected", name="approvalstatus"), server_default="pending"),
        sa.Column("reviewer_id", sa.Integer, sa.ForeignKey("users.id")),
        sa.Column("reviewed_at", sa.DateTime),
        sa.Column("notes", sa.String),
    )

def downgrade() -> None:
    op.drop_table("approvals")
    op.drop_table("proposals")
    op.drop_table("users")
