from typing import Annotated, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.security import get_authenticated_user
from app.database import get_database
from utils.crypt import get_bcrypt_context
from utils.exceptions.client import NotFoundException, UnauthorizedException
from utils.pagination import LimitOffsetPagination

from .dependencies import get_pagination, get_transaction_filter_manager, get_transaction_service
from .docs import (
    create_transaction_docs,
    destroy_transaction_docs,
    list_transaction_docs,
    retrieve_transaction_docs,
    update_transaction_docs,
)
from .filters import TransactionFilterManager, TransactionFilterSchema
from .models import Transaction as TransactionModel
from .schemas import TransactionSchema
from .services import TransactionService

router = APIRouter(prefix="/transaction", tags=["transaction"])

TransactionServiceAnnotation = Annotated[TransactionService, Depends(get_transaction_service)]


@router.get("/{id}", **retrieve_transaction_docs)
async def retrieve_transaction(id: int, service: TransactionServiceAnnotation):
    return service.retrieve_by_id(id=id)


@router.get("/", **list_transaction_docs)
async def list_transaction(
    service: TransactionServiceAnnotation,
    filter_manager: TransactionFilterManager = Depends(get_transaction_filter_manager),
    pagination_manager: LimitOffsetPagination = Depends(get_pagination),
):
    return service.list(filter_manager=filter_manager, pagination_manager=pagination_manager)


@router.post("/", **create_transaction_docs)
async def create_transaction(payload: TransactionSchema, service: TransactionServiceAnnotation):
    data = payload.model_dump()
    service.create(entity=data)
    return data


@router.put("/{id}", **update_transaction_docs)
async def update_transaction(id: int, payload: TransactionSchema, service: TransactionServiceAnnotation):
    data = payload.model_dump(exclude_unset=True)
    return service.update(id=id, entity=data)


@router.delete("/{id}", **destroy_transaction_docs)
async def destroy_transaction(id: int, service: TransactionServiceAnnotation):
    return service.destroy(id=id)
