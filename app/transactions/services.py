from utils.services import BaseService

from .models import Transaction
from .repository import TransactionRepository


class TransactionService(BaseService[Transaction, TransactionRepository]):
    pass
