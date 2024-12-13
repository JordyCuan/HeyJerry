from typing import Annotated, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.security import get_authenticated_user
from app.database import get_database
from utils.crypt import get_bcrypt_context
from utils.exceptions.client import NotFoundException, UnauthorizedException
from utils.pagination import LimitOffsetPagination

from .dependencies import get_account_service, get_pagination
from .docs import (
    create_account_docs,
    destroy_account_docs,
    list_account_docs,
    retrieve_account_docs,
    update_account_docs,
)
from .models import Account as AccountModel
from .schemas import AccountSchema
from .services import AccountService

router = APIRouter(prefix="/account", tags=["account"])

AccountServiceAnnotation = Annotated[AccountService, Depends(get_account_service)]


@router.get("/{id}", **retrieve_account_docs)
async def retrieve_account(id: int, service: AccountServiceAnnotation):
    return service.retrieve_by_id(id=id)


@router.get("/", **list_account_docs)
async def list_account(
    service: AccountServiceAnnotation,
    pagination_manager: LimitOffsetPagination = Depends(get_pagination),
):
    return service.list(pagination_manager=pagination_manager)


@router.post("/", **create_account_docs)
async def create_account(payload: AccountSchema, service: AccountServiceAnnotation):
    data = payload.model_dump()
    service.create(entity=data)
    return data


@router.put("/{id}", **update_account_docs)
async def update_account(id: int, payload: AccountSchema, service: AccountServiceAnnotation):
    data = payload.model_dump(exclude_unset=True)
    return service.update(id=id, entity=data)


@router.delete("/{id}", **destroy_account_docs)
async def destroy_account(id: int, service: AccountServiceAnnotation):
    return service.destroy(id=id)
