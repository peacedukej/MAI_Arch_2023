from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select, insert, delete
from rest_api.models.core import User
from rest_api.models.database import SessionLocal, engine, Base
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import rest_api.models.schemas as schemas 
from rest_api.controllers.connect_db import get_db

from passlib.context import CryptContext

# Создание экземпляра класса CryptContext для хэширования пароля
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


router = APIRouter()


responses = {
    422: {"description": "Не удалось записать данные"},
    423: {"description": "Не удалось прочитать данные"},
    424: {"description": "Пользователь с таким email уже зарегистрирован"},
}


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


    try:
        user_insert_query = insert(User).values(
            first_name=user_data.first_name,
            last_name=user_data.last_name,
            login=user_data.login,
            password=hashed_password,
        )

        result = await db.execute(user_insert_query)
        user_id = result.inserted_primary_key[0]
    except Exception as e:
        raise HTTPException(status_code=422,
                            detail=f"Не удалось записать данные, {e}")

    await db.commit()
