from typing import Optional

from fastapi import Depends, Query
from sqlalchemy.orm import Session

from app.database import get_database
from utils.pagination import LimitOffsetPagination, LimitOffsetSchema

from .repository import AccountRepository
from .services import AccountService


def get_account_repository(session: Session = Depends(get_database)) -> AccountRepository:
    return AccountRepository(session=session)


def get_account_service(repository: AccountRepository = Depends(get_account_repository)) -> AccountService:
    return AccountService(repository=repository)


# TODO: This one might be "global" for project due its (possible) immutability across domains nature
def get_pagination(pagination: LimitOffsetSchema = Depends()) -> LimitOffsetPagination:
    return LimitOffsetPagination(pagination)
