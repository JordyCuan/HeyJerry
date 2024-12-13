from utils.database.repository import BaseRepository

from .models import Tag


class TagRepository(BaseRepository[Tag]):
    model = Tag
