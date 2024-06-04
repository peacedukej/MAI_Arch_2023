from fastapi import FastAPI
from rest_api.routers.user_router import router as user_router

app = FastAPI()

# Регистрация роутера в основном приложении
app.include_router(user_router)
