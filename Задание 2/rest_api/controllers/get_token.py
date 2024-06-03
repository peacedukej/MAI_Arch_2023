from fastapi import HTTPException, Depends, Request, status
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from jose import jwt, JWTError
from rest_api.models.core import User
from rest_api.config import SECRET_KEY, ALGORITHM
from sqlalchemy.ext.asyncio import AsyncSession
from rest_api.models.database import SessionLocal, engine, Base


bearer_scheme = HTTPBearer()

# Функция для проверки JWT токена
def verify_token(credentials: HTTPAuthorizationCredentials = Depends(bearer_scheme)):
    token = credentials.credentials
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Если токен успешно декодирован, возвращаем данные из токена
        return payload
    except JWTError:
        # Если произошла ошибка при декодировании токена, возвращаем HTTP-ошибку 401 Unauthorized
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"},
        )
