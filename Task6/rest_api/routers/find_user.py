from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy import select, insert, delete
from rest_api.models.core import User
from rest_api.models.database import SessionLocal, engine, Base
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import rest_api.models.schemas as schemas 
from rest_api.controllers.connect_db import get_db
from typing import Optional, Dict, Any, List
router = APIRouter()


responses = {
    422: {"description": "Не удалось записать данные"},
    423: {"description": "Не удалось прочитать данные"},
    424: {"description": "Пользователь с таким email уже зарегистрирован"},
}

from sqlalchemy import or_

# Поиск пользователей по маске фамилии и имени
@router.get("/", responses=responses)
async def search_users(name_mask: str, db: AsyncSession = Depends(get_db)):
    try:
        users = await db.execute(select(User).filter(or_(User.first_name.ilike(f'%{name_mask}%'), User.last_name.ilike(f'%{name_mask}%'))))
        users = users.scalars().all()
    except Exception as e:
        raise HTTPException(status_code=500, detail="Ошибка сервера")
    
    return users
