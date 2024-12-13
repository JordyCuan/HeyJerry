from enum import Enum
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class CategoryType(str, Enum):
    income = "Income"
    expense = "Expense"
    transfer = "Transfer"


class CategorySchema(BaseModel):
    name: str = Field(..., description="Name of the category")
    description: Optional[str] = Field(None, description="Optional description of the category")
    type: CategoryType

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"name": "Salary", "description": "Monthly salary payments", "type": "Income"},
                {"name": "Groceries", "description": "Food and supplies expenses", "type": "Expense"},
            ]
        }
    )
