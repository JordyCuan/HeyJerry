from typing import Any, Generic, Optional, Protocol, TypeVar

from sqlalchemy.orm import DeclarativeBase

from .database.repository import FilterManagerProtocol, PaginationManagerProtocol

ModelType = TypeVar("ModelType", bound=DeclarativeBase)
RepositoryType = TypeVar("RepositoryType", bound="RepositoryProtocol")


class RepositoryProtocol(Protocol):  # pragma: no cover
    def retrieve_by_id(self, *, id: int) -> DeclarativeBase:
        pass

    def retrieve(self, **filters: Any) -> DeclarativeBase:
        pass

    def list(
        self,
        *,
        filter_manager: Optional[FilterManagerProtocol] = None,
        pagination_manager: Optional[PaginationManagerProtocol] = None,
        **filters: Any,
    ) -> list[DeclarativeBase]:
        pass

    def create(self, *, entity: dict[str, Any]) -> DeclarativeBase:
        pass

    def update(self, *, id: int, entity: dict[str, Any]) -> DeclarativeBase:
        pass

    def destroy(self, *, id: int) -> None:
        pass

    def perform_commit(self) -> None:
        pass


class BaseService(Generic[ModelType, RepositoryType]):
    def __init__(self, *, repository: RepositoryType):
        self.repository = repository

    def retrieve_by_id(self, *, id: int) -> ModelType:
        return self.repository.retrieve_by_id(id=id)  # type: ignore

    def get(self, **filters: Any) -> ModelType:
        return self.repository.retrieve(**filters)  # type: ignore

    def list(
        self,
        filter_manager: Optional[FilterManagerProtocol] = None,
        pagination_manager: Optional[PaginationManagerProtocol] = None,
        **filters: Any,
    ) -> list[ModelType]:
        return self.repository.list(
            filter_manager=filter_manager, pagination_manager=pagination_manager, **filters
        )  # type: ignore

    def create(self, *, entity: dict[str, Any]) -> ModelType:
        instance = self.repository.create(entity=entity)
        self.repository.perform_commit()
        return instance  # type: ignore

    def update(self, *, id: int, entity: dict[str, Any]) -> ModelType:
        instance = self.repository.update(id=id, entity=entity)
        self.repository.perform_commit()
        return instance  # type: ignore

    def destroy(self, *, id: int) -> None:
        self.repository.destroy(id=id)
        self.repository.perform_commit()
