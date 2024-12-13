from pydantic import BaseModel, ConfigDict, Field


class TagSchema(BaseModel):
    name: str = Field(..., description="Name of the tag")

    model_config = ConfigDict(
        json_schema_extra={
            "examples": [
                {"name": "Urgent"},
                {"name": "Tax Deductible"},
            ]
        }
    )
