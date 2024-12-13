from typing import Annotated, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.security import get_authenticated_user
from app.database import get_database
from utils.crypt import get_bcrypt_context
from utils.exceptions.client import NotFoundException, UnauthorizedException
from utils.pagination import LimitOffsetPagination

from .dependencies import get_category_service, get_pagination
from .docs import (
    create_category_docs,
    destroy_category_docs,
    list_category_docs,
    retrieve_category_docs,
    update_category_docs,
)
from .models import Category as CategoryModel
from .schemas import CategorySchema
from .services import CategoryService

router = APIRouter(prefix="/category", tags=["category"])

CategoryServiceAnnotation = Annotated[CategoryService, Depends(get_category_service)]


@router.get("/{id}", **retrieve_category_docs)
async def retrieve_category(id: int, service: CategoryServiceAnnotation):
    return service.retrieve_by_id(id=id)


@router.get("/", **list_category_docs)
async def list_category(
    service: CategoryServiceAnnotation,
    pagination_manager: LimitOffsetPagination = Depends(get_pagination),
):
    return service.list(pagination_manager=pagination_manager)


@router.post("/", **create_category_docs)
async def create_category(payload: CategorySchema, service: CategoryServiceAnnotation):
    data = payload.model_dump()
    service.create(entity=data)
    return data


@router.put("/{id}", **update_category_docs)
async def update_category(id: int, payload: CategorySchema, service: CategoryServiceAnnotation):
    data = payload.model_dump(exclude_unset=True)
    return service.update(id=id, entity=data)


@router.delete("/{id}", **destroy_category_docs)
async def destroy_category(id: int, service: CategoryServiceAnnotation):
    return service.destroy(id=id)
