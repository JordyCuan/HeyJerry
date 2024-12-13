from typing import Annotated, Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.auth.security import get_authenticated_user
from app.database import get_database
from utils.crypt import get_bcrypt_context
from utils.exceptions.client import NotFoundException, UnauthorizedException
from utils.pagination import LimitOffsetPagination

from .dependencies import get_pagination, get_tag_filter_manager, get_tag_service
from .docs import create_tag_docs, destroy_tag_docs, list_tag_docs, retrieve_tag_docs, update_tag_docs
from .filters import TagFilterManager, TagFilterSchema
from .models import Tag as TagModel
from .schemas import TagSchema
from .services import TagService

router = APIRouter(prefix="/tag", tags=["tag"])

TagServiceAnnotation = Annotated[TagService, Depends(get_tag_service)]


@router.get("/{id}", **retrieve_tag_docs)
async def retrieve_tag(id: int, service: TagServiceAnnotation):
    return service.retrieve_by_id(id=id)


@router.get("/", **list_tag_docs)
async def list_tag(
    service: TagServiceAnnotation,
    filter_manager: TagFilterManager = Depends(get_tag_filter_manager),
    pagination_manager: LimitOffsetPagination = Depends(get_pagination),
):
    return service.list(filter_manager=filter_manager, pagination_manager=pagination_manager)


@router.post("/", **create_tag_docs)
async def create_tag(payload: TagSchema, service: TagServiceAnnotation):
    data = payload.model_dump()
    service.create(entity=data)
    return data


@router.put("/{id}", **update_tag_docs)
async def update_tag(id: int, payload: TagSchema, service: TagServiceAnnotation):
    data = payload.model_dump(exclude_unset=True)
    return service.update(id=id, entity=data)


@router.delete("/{id}", **destroy_tag_docs)
async def destroy_tag(id: int, service: TagServiceAnnotation):
    return service.destroy(id=id)
