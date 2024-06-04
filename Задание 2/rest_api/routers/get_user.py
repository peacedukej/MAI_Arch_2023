from fastapi import APIRouter, HTTPException, Depends, status, Query
from sqlalchemy import select, insert, delete
from rest_api.models.core import User
from rest_api.models.database import SessionLocal, engine, Base
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import rest_api.models.schemas as schemas 
from rest_api.controllers.connect_db import get_db
from jose import jwt
from datetime import datetime, timedelta
from rest_api.config import SECRET_KEY, ALGORITHM, JWT_EXPIRATION_TIME_MINUTES
from passlib.context import CryptContext
from rest_api.redis.redis import redis  
import json

# Создание экземпляра класса CryptContext для хэширования пароля
#r = redis.Redis(host='redis', port=6379, db=0)

router = APIRouter()


responses = {
    422: {"description": "Не удалось записать данные"},
    423: {"description": "Не удалось прочитать данные"},
    424: {"description": "Пользователь с таким email уже зарегистрирован"},
}


@router.get("/get", responses=responses)
async def get_user(id: int = Query(..., description="ID пользователя"), db: AsyncSession = Depends(get_db)):
    # Попытка получить данные пользователя из Redis
    #cached_user = await redis.hgetall(f"user:{id}")
    #if cached_user:
    #    return cached_user

    try:
        user_select_query = select(User).where(User.user_id == id)
        query_result = await db.execute(user_select_query)
        result = query_result.scalars().first()
    except Exception as e:
        raise HTTPException(status_code=422, detail=f"Не удалось записать данные, {e}")

    if not result:
        raise HTTPException(status_code=404, detail="Пользователь не найден")

    user_dict = {
        "first_name": result.first_name if hasattr(result, 'first_name') and result.first_name else "",
        "last_name": result.last_name if hasattr(result, 'last_name') and result.last_name else "",
        "login": result.login if hasattr(result, 'login') and result.login else "",
        "hashed_password": result.hashed_password if hasattr(result, 'hashed_password') and result.hashed_password else "",
        "token": result.token if hasattr(result, 'token') and result.token else "",
    }

    #await redis.hset(f"user:{id}", mapping=user_dict)
    
    return user_dict
 