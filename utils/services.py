from typing import Any, Generic, Optional, Protocol, TypeVar

from sqlalchemy.orm import DeclarativeBase

from .database.repository import FilterManagerProtocol, PaginationManagerProtocol

RepositoryType = TypeVar("RepositoryType", bound="RepositoryProtocol")


class RepositoryProtocol(Protocol):  # pragma: no cover
    # TODO: Fix types using `TypeVars` rather than generic `DeclarativeBase`
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

    # TODO: Fix types to avoid dumping everything into this Protocol class
    def perform_commit(self) -> None:
        pass


class BaseService(Generic[RepositoryType]):
    def __init__(self, *, repository: RepositoryType):
        self.repository = repository

    def retrieve_by_id(self, *, id: int) -> DeclarativeBase:
        return self.repository.retrieve_by_id(id=id)

    def get(self, **filters: Any) -> DeclarativeBase:
        return self.repository.retrieve(**filters)

    def list(
        self,
        filter_manager: Optional[FilterManagerProtocol] = None,
        pagination_manager: Optional[PaginationManagerProtocol] = None,
        **filters: Any,
    ) -> list[DeclarativeBase]:
        return self.repository.list(
            filter_manager=filter_manager, pagination_manager=pagination_manager, **filters
        )

    def create(self, *, entity: dict[str, Any]) -> DeclarativeBase:
        instance = self.repository.create(entity=entity)
        self.repository.perform_commit()
        return instance  # NOTE: ~Maybe we want to return~

    def update(self, *, id: int, entity: dict[str, Any]) -> DeclarativeBase:
        instance = self.repository.update(id=id, entity=entity)
        self.repository.perform_commit()
        return instance

    def destroy(self, *, id: int) -> None:
        self.repository.destroy(id=id)
        self.repository.perform_commit()
