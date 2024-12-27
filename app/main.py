from fastapi import FastAPI

from app.accounts.router import router as accounts_router
from app.auth.router import router as auth_router
from app.categories.router import router as categories_router
from app.settings import settings
from app.transactions.router import router as transactions_router
from app.users.router import router as users_router
from utils.middleware import SQLAlchemyExceptionHandlerMiddleware

app = FastAPI(debug=settings.DEBUG)


app.add_middleware(SQLAlchemyExceptionHandlerMiddleware, debug=settings.DEBUG)

app.include_router(auth_router)
app.include_router(accounts_router)
app.include_router(categories_router)
app.include_router(transactions_router)
app.include_router(users_router)
