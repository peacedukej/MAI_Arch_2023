from fastapi import APIRouter, HTTPException, Depends, status
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
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter()


responses = {
    422: {"description": "Не удалось записать данные"},
    423: {"description": "Не удалось прочитать данные"},
    424: {"description": "Пользователь с таким email уже зарегистрирован"},
}

def create_jwt_token(username: str) -> str:
    expiration_time = datetime.utcnow() + timedelta(minutes=JWT_EXPIRATION_TIME_MINUTES)
    payload = {"sub": username, "exp": expiration_time}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


async def get_user_from_cache(login: str):
    user_json = await redis.get(f"user:{login}")
    if user_json:
        user_data = json.loads(user_json)
        return user_data
    return None

async def set_user_to_cache(user_data: dict):
    await redis.set(f"user:{user_data['login']}", json.dumps(user_data), ex=60*60)  # Кешируем на 1 час


@router.post("/", responses=responses)
async def register_user(user_data: schemas.Registration, db: AsyncSession = Depends(get_db)):
    try:
        existing_user = await db.execute(select(User).filter(User.login == user_data.login))
        existing_user = existing_user.scalars().first()
    except Exception as e:
        raise HTTPException(status_code=423,
                           detail="Не удалось прочитать данные")
    if existing_user:
       raise HTTPException(status_code=424,
                           detail="Пользователь с таким login уже зарегистрирован")


# Хэширование пароля
    hashed_password = pwd_context.hash(user_data.password)
    token = create_jwt_token(user_data.login)

    try:
        user_insert_query = insert(User).values(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            login=user_data.login,
            password=hashed_password,
            token = token
        )

        result = await db.execute(user_insert_query)
        user_id = result.inserted_primary_key[0]
    except Exception as e:
        raise HTTPException(status_code=422,
                            detail=f"Не удалось записать данные, {e}")

    await db.commit()

    user_dict = {
        "first_name": user_data.first_name,
        "last_name": user_data.last_name,
        "login": user_data.login,
        "hashed_password": hashed_password,
        "token": token,
    }

    # Кешируем данные пользователя
    await set_user_to_cache(user_dict)

    return user_dict
