from utils.database.repository import BaseRepository

from .models import Account


class AccountRepository(BaseRepository[Account]):
    model = Account
