from utils.services import BaseService

from .models import Category
from .repository import CategoryRepository


class CategoryService(BaseService[Category, CategoryRepository]):
    pass
