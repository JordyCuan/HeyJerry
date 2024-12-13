from typing import Optional

from fastapi import Depends, Query
from sqlalchemy.orm import Session

from app.database import get_database
from utils.pagination import LimitOffsetPagination, LimitOffsetSchema

from .repository import CategoryRepository
from .services import CategoryService


def get_category_repository(session: Session = Depends(get_database)) -> CategoryRepository:
    return CategoryRepository(session=session)


def get_category_service(
    repository: CategoryRepository = Depends(get_category_repository),
) -> CategoryService:
    return CategoryService(repository=repository)


# TODO: This one might be "global" for project due its (possible) immutability across domains nature
def get_pagination(pagination: LimitOffsetSchema = Depends()) -> LimitOffsetPagination:
    return LimitOffsetPagination(pagination)
