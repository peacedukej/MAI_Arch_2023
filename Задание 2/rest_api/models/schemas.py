# fast_api/models/schemas.py
from pydantic import BaseModel, Field
from typing import Optional, Dict, Any, List
    

class Registration(BaseModel):
    first_name: str
    last_name: str
    login: str
    password: str
    #token: str

# Схема данных пользователя для обновления
class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    login: Optional[str] = None
    password: Optional[str] = None

# Схема данных пользователя для ответа
class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    login: str

# Схема данных для поиска пользователей
class UserSearch(BaseModel):
    name_mask: str
