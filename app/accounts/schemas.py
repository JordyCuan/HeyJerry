from typing import Optional

from pydantic import BaseModel, ConfigDict, Field


class AccountSchema(BaseModel):
    user_id: int
    name: str = Field(..., description="Name of the account")
    description: Optional[str] = Field(None, description="Optional description of the account")
    # is_active: Optional[bool] = Field(True, description="Is this account active?")
    initial_balance: float = Field(..., description="The starting balance of the account")
    current_balance: float = Field(..., description="The current balance of the account")

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {
                    "user_id": 1,
                    "name": "Checking Account",
                    "description": "Main account for daily expenses",
                    "initial_balance": 1000.0,
                    "current_balance": 1200.0,
                },
                {
                    "user_id": 2,
                    "name": "Savings Account",
                    "description": "Account for saving funds",
                    "initial_balance": 5000.0,
                    "current_balance": 5100.0,
                },
            ]
        }
    )
