from typing import Optional

from fastapi import Depends, Query
from sqlalchemy.orm import Session

from app.database import get_database
from utils.pagination import LimitOffsetPagination, LimitOffsetSchema

from .filters import TagFilterManager, TagFilterSchema
from .repository import TagRepository
from .services import TagService


def get_tag_repository(session: Session = Depends(get_database)) -> TagRepository:
    return TagRepository(session=session)


def get_tag_service(repository: TagRepository = Depends(get_tag_repository)) -> TagService:
    return TagService(repository=repository)


def get_tag_filter_manager(
    filters: TagFilterSchema = Depends(),
    ordering: Optional[list[str]] = Query(None),
) -> TagFilterManager:
    return TagFilterManager(filters=filters, ordering=ordering)


# TODO: This one might be "global" for project due its (possible) immutability across domains nature
def get_pagination(pagination: LimitOffsetSchema = Depends()) -> LimitOffsetPagination:
    return LimitOffsetPagination(pagination)
