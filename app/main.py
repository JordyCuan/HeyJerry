from fastapi import FastAPI

from app.accounts.router import router as accounts_router
from app.auth.router import router as auth_router
from app.categories.router import router as categories_router
from app.database import Base, engine
from app.settings import settings

# from app.tags.router import router as tags_router
from app.transactions.router import router as transactions_router
from app.users.router import router as users_router
from utils.middleware import SQLAlchemyExceptionHandlerMiddleware

app = FastAPI(debug=settings.DEBUG)

# Base.metadata.create_all(bind=engine)  # NOTE: Do we really need this? Apparently just for models init

app.add_middleware(SQLAlchemyExceptionHandlerMiddleware, debug=settings.DEBUG)

app.include_router(auth_router)
app.include_router(accounts_router)
app.include_router(categories_router)
# app.include_router(tags_router)
app.include_router(transactions_router)
app.include_router(users_router)
