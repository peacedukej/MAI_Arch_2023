from fastapi import APIRouter, HTTPException
from pymongo import MongoClient
from pydantic import BaseModel
from rest_api.models.schemas import User
router = APIRouter()

client = MongoClient("mongodb", 27017)
db = client["mydatabase"]
users = db["users"]

class User(BaseModel):
    username: str
    email: str
    password: str

@router.get("/users/{username}")
async def read_user(username: str):
    user = users.find_one({"username": username})
    if user:
        user_dict = {
            "username": user["username"],
            "email": user["email"],
            # Другие поля, если есть
        }
        return user_dict
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/users/")
async def create_user(user: User):
    user_data = user.dict()
    inserted_id = users.insert_one(user_data).inserted_id
    return {"id": str(inserted_id)}

@router.put("/users/{username}")
async def update_user(username: str, user: User):
    user_data = user.dict()
    result = users.update_one({"username": username}, {"$set": user_data})
    if result.modified_count == 1:
        return {"message": "User updated successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{username}")
async def delete_user(username: str):
    result = users.delete_one({"username": username})
    if result.deleted_count == 1:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")
