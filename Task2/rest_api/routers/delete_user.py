from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select, insert, delete
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

# Удаление пользователя
@router.delete("/", responses=responses)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    #try:
    await db.execute(delete(User).where(User.user_id == user_id))
    await db.commit()
    #except Exception as e:
        #raise HTTPException(status_code=500, detail="Ошибка сервера")