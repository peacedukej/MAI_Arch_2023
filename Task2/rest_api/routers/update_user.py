from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select, insert, delete, update
from rest_api.models.core import User
from rest_api.models.database import SessionLocal, engine, Base
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import rest_api.models.schemas as schemas 
from rest_api.controllers.connect_db import get_db
router = APIRouter()


responses = {
    422: {"description": "Не удалось записать данные"},
    423: {"description": "Не удалось прочитать данные"},
    424: {"description": "Пользователь с таким email уже зарегистрирован"},
}

# Обновление данных пользователя
@router.put("/", responses=responses)
async def update_user(user_id: int, user_data: schemas.UserUpdate, db: AsyncSession = Depends(get_db)):
    #try:
    await db.execute(update(User).where(User.user_id == user_id).values(**user_data.dict(exclude_unset=True)))
    await db.commit()
    #except Exception as e:
        #raise HTTPException(status_code=500, detail="Ошибка сервера")