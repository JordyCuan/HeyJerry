from typing import Any

from sqlalchemy.orm import DeclarativeBase, declared_attr


class APIBaseModel(DeclarativeBase):
    id: Any
    __name__: str

    @declared_attr.directive
    def __tablename__(cls) -> str:
        return cls.__name__
