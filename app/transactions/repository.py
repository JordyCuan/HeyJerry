from utils.database.repository import BaseRepository

from .models import Transaction


class TransactionRepository(BaseRepository[Transaction]):
    model = Transaction
