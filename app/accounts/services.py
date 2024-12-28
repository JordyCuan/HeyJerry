from utils.services import BaseService

from .models import Account
from .repository import AccountRepository


class AccountService(BaseService[Account, AccountRepository]):
    pass
