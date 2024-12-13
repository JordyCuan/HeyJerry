from datetime import date
from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class TransactionType(str, Enum):
    income = "Income"
    expense = "Expense"
    transfer = "Transfer"


class TransactionSchema(BaseModel):
    account_id: int
    user_id: int
    category_id: int
    amount: float = Field(description="Transaction amount must be non-negative")
    transaction_type: TransactionType
    description: Optional[str] = Field(None, description="Optional transaction description")
    date: date

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "account_id": 1,
                    "user_id": 1,
                    "category_id": 1,
                    "amount": 100.50,
                    "transaction_type": "Income",
                    "description": "Monthly salary",
                    "date": "2024-12-01",
                },
                {
                    "account_id": 2,
                    "user_id": 1,
                    "category_id": 2,
                    "amount": -50.00,
                    "transaction_type": "Expense",
                    "description": "Grocery shopping",
                    "date": "2024-12-03",
                },
            ]
        }
    )
