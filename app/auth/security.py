from datetime import datetime, timedelta, timezone
from typing import Any, Optional

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt

from app.settings import settings
from utils.crypt import get_bcrypt_context
from utils.exceptions.client import ForbiddenException, UnauthorizedException

bcrypt_context = get_bcrypt_context(schemes=["bcrypt"], deprecated="auto")


oauth_bearer = OAuth2PasswordBearer(tokenUrl="token")


def create_access_token(username: str, user_id: int, expires_delta: Optional[timedelta] = None) -> str:
    encode: dict[str, str | int | datetime] = {"sub": username, "id": user_id}
    now = datetime.now(timezone.utc)

    expire = now + timedelta(minutes=15)
    if expires_delta:
        expire = now + expires_delta

    encode.update({"exp": expire})
    return jwt.encode(encode, settings.SECRET_KEY, algorithm=settings.JWT_ALGORITHM)


def get_authenticated_user(token: str = Depends(oauth_bearer)) -> dict[str, str | int]:
    try:
        payload: dict[str, Any] = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.JWT_ALGORITHM])
        username = payload.get("sub")
        user_id = payload.get("id")
        if username is None or user_id is None:
            raise UnauthorizedException
        return {"username": username, "id": user_id}
    except JWTError as exc:
        raise ForbiddenException(detail="Could not validate credentials") from exc
