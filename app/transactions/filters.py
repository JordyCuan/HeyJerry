from typing import Annotated, Optional

from fastapi import Query

from utils.filters import BaseFilterManager, FilterSchema

from .models import Transaction


class TransactionFilterSchema(FilterSchema, extra="forbid"):
    transaction_type__ieq: Optional[str] = Query(None)
    date__gt: Optional[int] = Query(None)
    date__gte: Optional[int] = Query(None)
    date__lt: Optional[int] = Query(None)
    date__lte: Optional[int] = Query(None)
    date__eq: Optional[int] = Query(None)
    description__contains: Annotated[str | None, Query(None)]
    description__icontains: Optional[str] = Query(None)


class TransactionFilterManager(BaseFilterManager):
    model = Transaction
