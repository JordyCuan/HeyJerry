from datetime import datetime
from typing import TYPE_CHECKING, Optional

from sqlalchemy import Date, Enum, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

if TYPE_CHECKING:
    from app.accounts.models import Account  # noqa: F401
    from app.categories.models import Category  # noqa: F401
    from app.tags.models import Tag  # noqa: F401
    from app.users.models import User  # noqa: F401


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    account_id: Mapped[int] = mapped_column(ForeignKey("accounts.id"), nullable=False)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), nullable=False)
    category_id: Mapped[int] = mapped_column(ForeignKey("categories.id"), nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)
    transaction_type: Mapped[str] = mapped_column(
        Enum("Income", "Expense", "Transfer", name="transaction_type"), nullable=False
    )
    description: Mapped[Optional[str]] = mapped_column(nullable=True)
    date: Mapped[datetime] = mapped_column(Date, nullable=False, default=datetime.utcnow)

    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)
    updated_at: Mapped[datetime] = mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)

    account: Mapped["Account"] = relationship(back_populates="transactions")
    user: Mapped["User"] = relationship(back_populates="transactions")
    category: Mapped["Category"] = relationship(back_populates="transactions")
    transaction_tags: Mapped[list["TransactionTag"]] = relationship(
        "TransactionTag",  #
        back_populates="transaction",
    )


# class TransactionTag(Base):
#     __tablename__ = "transaction_tags"

#     id: Mapped[int] = mapped_column(primary_key=True, index=True)
#     transaction_id: Mapped[int] = mapped_column(ForeignKey("transactions.id"), nullable=False)
#     tag_id: Mapped[int] = mapped_column(ForeignKey("tags.id"), nullable=False)
#     transaction: Mapped["Transaction"] = relationship(back_populates="transaction_tags")
#     tag: Mapped["Tag"] = relationship(back_populates="transaction_tags")
