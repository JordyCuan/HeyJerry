from typing import Optional

from fastapi import Depends, Query
from sqlalchemy.orm import Session

from app.database import get_database
from utils.pagination import LimitOffsetPagination, LimitOffsetSchema

from .filters import TransactionFilterManager, TransactionFilterSchema
from .repository import TransactionRepository
from .services import TransactionService


def get_transaction_repository(session: Session = Depends(get_database)) -> TransactionRepository:
    return TransactionRepository(session=session)


def get_transaction_service(
    repository: TransactionRepository = Depends(get_transaction_repository),
) -> TransactionService:
    return TransactionService(repository=repository)


def get_transaction_filter_manager(
    filters: TransactionFilterSchema = Depends(),
    ordering: Optional[list[str]] = Query(None),
) -> TransactionFilterManager:
    return TransactionFilterManager(filters=filters, ordering=ordering)


# TODO: This one might be "global" for project due its (possible) immutability across domains nature
def get_pagination(pagination: LimitOffsetSchema = Depends()) -> LimitOffsetPagination:
    return LimitOffsetPagination(pagination)
