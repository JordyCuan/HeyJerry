from typing import Annotated, Optional

from fastapi import Query

from utils.filters import BaseFilterManager, FilterSchema

from .models import Tag


class TagFilterSchema(FilterSchema, extra="forbid"):
    name__ieq: Optional[str] = Query(None)
    name__icontains: Optional[str] = Query(None)


class TagFilterManager(BaseFilterManager):
    model = Tag
