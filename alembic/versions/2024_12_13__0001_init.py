"""Init

Revision ID: 2f0b48ffdc66
Revises:
Create Date: 2024-12-13 19:00:47.195145

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

revision = "2f0b48ffdc66"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('users_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("email", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("username", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("hashed_password", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("firstname", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("lastname", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("is_active", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column("created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column("updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.PrimaryKeyConstraint("id", name="users_pkey"),
        sa.UniqueConstraint("username", name="users_username_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_users_id", "users", ["id"], unique=False)
    op.create_index("ix_users_email", "users", ["email"], unique=True)
    op.create_table(
        "accounts",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('accounts_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("description", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("initial_balance", sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
        sa.Column("current_balance", sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
        sa.Column("is_active", sa.BOOLEAN(), autoincrement=False, nullable=True),
        sa.Column("created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column("updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="accounts_user_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="accounts_pkey"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_accounts_id", "accounts", ["id"], unique=False)
    op.create_table(
        "categories",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('categories_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("description", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column(
            "type",
            postgresql.ENUM("Income", "Expense", "Transfer", name="category_type"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column("updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="categories_user_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="categories_pkey"),
        sa.UniqueConstraint("name", name="categories_name_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_categories_id", "categories", ["id"], unique=False)
    op.create_table(
        "transactions",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("account_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("category_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("amount", sa.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
        sa.Column(
            "transaction_type",
            postgresql.ENUM("Income", "Expense", "Transfer", name="transaction_type"),
            autoincrement=False,
            nullable=False,
        ),
        sa.Column("description", sa.VARCHAR(), autoincrement=False, nullable=True),
        sa.Column("date", sa.DATE(), autoincrement=False, nullable=False),
        sa.Column("created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column("updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(["account_id"], ["accounts.id"], name="transactions_account_id_fkey"),
        sa.ForeignKeyConstraint(["category_id"], ["categories.id"], name="transactions_category_id_fkey"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="transactions_user_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="transactions_pkey"),
    )
    op.create_index("ix_transactions_id", "transactions", ["id"], unique=False)
    op.create_table(
        "tags",
        sa.Column(
            "id",
            sa.INTEGER(),
            server_default=sa.text("nextval('tags_id_seq'::regclass)"),
            autoincrement=True,
            nullable=False,
        ),
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
        sa.Column("user_id", sa.INTEGER(), autoincrement=False, nullable=True),
        sa.Column("created_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.Column("updated_at", postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], name="tags_user_id_fkey"),
        sa.PrimaryKeyConstraint("id", name="tags_pkey"),
        sa.UniqueConstraint("name", name="tags_name_key"),
        postgresql_ignore_search_path=False,
    )
    op.create_index("ix_tags_id", "tags", ["id"], unique=False)
    op.create_table(
        "transaction_tags",
        sa.Column("id", sa.INTEGER(), autoincrement=True, nullable=False),
        sa.Column("transaction_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.Column("tag_id", sa.INTEGER(), autoincrement=False, nullable=False),
        sa.ForeignKeyConstraint(["tag_id"], ["tags.id"], name="transaction_tags_tag_id_fkey"),
        sa.ForeignKeyConstraint(
            ["transaction_id"], ["transactions.id"], name="transaction_tags_transaction_id_fkey"
        ),
        sa.PrimaryKeyConstraint("id", name="transaction_tags_pkey"),
    )
    op.create_index("ix_transaction_tags_id", "transaction_tags", ["id"], unique=False)


def downgrade() -> None:
    op.drop_index("ix_transaction_tags_id", table_name="transaction_tags")
    op.drop_table("transaction_tags")

    op.drop_index("ix_transactions_id", table_name="transactions")
    op.drop_table("transactions")
    op.drop_index("ix_categories_id", table_name="categories")
    op.drop_table("categories")

    op.drop_index("ix_tags_id", table_name="tags")
    op.drop_table("tags")

    op.drop_index("ix_accounts_id", table_name="accounts")
    op.drop_table("accounts")

    op.drop_index("ix_users_email", table_name="users")
    op.drop_index("ix_users_id", table_name="users")
    op.drop_table("users")
