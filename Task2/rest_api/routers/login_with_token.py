from fastapi import APIRouter, HTTPException, Depends, Header
from sqlalchemy import select, insert, update
from rest_api.models.core import User
from rest_api.models.database import SessionLocal, engine, Base
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import datetime
import rest_api.models.schemas as schemas # Импортируем созданную модель
from fastapi.responses import JSONResponse
from jose import jwt
from datetime import datetime, timedelta
from rest_api.config import SECRET_KEY, ALGORITHM, JWT_EXPIRATION_TIME_MINUTES
from rest_api.controllers.get_token import verify_token
from rest_api.controllers.connect_db import get_db

router = APIRouter()


# async def get_db(): 
#     async with engine.begin() as connection:
#         await connection.run_sync(Base.metadata.create_all)
    
#     db = SessionLocal() 
#     try: 
#         yield db 
#     finally: 
#         await db.close()


responses = {
    401: {"description": "Требуется авторизация"},
    402: {"description": "Неверный логин или пароль"},
    403: {"description": "Невалидный токен"},
    422: {"description": "Не удалось записать данные"},
    423: {"description": "Не удалось прочитать данные"},
    424: {"description": "Пользователь с таким email уже зарегистрирован"},
    425: {"description": "Организация уже зарегистрирована"},
    426: {"description": "Не удалось сформировать токен"},
    427: {"description": "Не удалось обновить данные"},
    428: {"description": "Такого пользователя не существует"}
}


@router.get("/")
async def authorize_with_token(token_data: dict = Depends(verify_token), db: AsyncSession = Depends(get_db)):
    try:
        login = token_data.get("sub")
    except Exception as e:
        raise HTTPException(status_code=403, detail="Невалидный токен")
    
    try:
        user_query = select(User).where(User.login == login)
        user_result = await db.execute(user_query)
        user = user_result.scalars().first()  # Получаем первую строку (первого пользователя)
    except Exception as e:
        raise HTTPException(status_code=423, detail="Не удалось прочитать данные")
    if user is None:
        raise HTTPException(status_code=428, detail="Такого пользователя не существует")
    
    # last_name = user.last_name + " "
    # first_name = user.first_name[0] + ". " if user.patronymic else user.first_name[0] + "."
    # patronymic = user.patronymic[0] + "." if user.patronymic else ""
    # return {
    #         "avatar": user.avatar_path,
    #         "fio": (last_name + first_name + patronymic).title()}

