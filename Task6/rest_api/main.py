from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware


from rest_api.routers.register_user import router as register_users_router
from rest_api.routers.delete_user import router as delete_users_router
from rest_api.routers.update_user import router as update_users_router
from rest_api.routers.find_user import router as find_users_router
from rest_api.routers.login_with_token import router as login_with_token_router
from rest_api.routers.get_user import router as get_user_router


app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)


app.include_router(
    router=register_users_router,
    tags=["Добавить"], 
    prefix="/add",
)

app.include_router(
    router=login_with_token_router,
    tags=["Авторизация через токен"], 
    prefix="/token",
)

app.include_router(
    router=delete_users_router,
    tags=["Удалить"], 
    prefix="/delete",
)

app.include_router(
    router=update_users_router,
    tags=["Обновить"], 
    prefix="/update",
)

app.include_router(
    router=find_users_router,
    tags=["Найти по маске"], 
    prefix="/find",
)


app.include_router(
    router=get_user_router,
    tags=["Получить данные о пользователе по ID"], 
    prefix="/get",
)
