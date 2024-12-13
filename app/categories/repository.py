from utils.database.repository import BaseRepository

from .models import Category


class CategoryRepository(BaseRepository[Category]):
    model = Category
