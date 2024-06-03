from fastapi import FastAPI, Depends
#from rest_api.models import core
#from rest_api.models.database import engine
from fastapi.middleware.cors import CORSMiddleware
#from rest_api.config import SECRET_KEY, ALGORITHM, JWT_EXPIRATION_TIME_MINUTES

from rest_api.routers.register_user import router as register_users_router
from rest_api.routers.delete_user import router as delete_users_router
from rest_api.routers.update_user import router as update_users_router
from rest_api.routers.find_user import router as find_users_router
#from rest_api.models.database import init_db



app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"], 
)

# @app.on_event("startup")
# async def on_startup():
#     # Инициализация базы данных
#     await init_db()

# '''
# Авторизация

# '''


# app.include_router(
#     router=authorization_router,
#     tags=["Авторизация"], 
#     prefix="/account_api/login",
# )

# app.include_router(
#     router=authorize_with_token_router,
#     tags=["Авторизация"],
#     prefix='/account_api/login_with_token',
# )



app.include_router(
    router=register_users_router,
    tags=["Регистрация"], 
    prefix="/add",
)

app.include_router(
    router=delete_users_router,
    tags=["Регистрация"], 
    prefix="/delete",
)

app.include_router(
    router=update_users_router,
    tags=["Регистрация"], 
    prefix="/update",
)

app.include_router(
    router=find_users_router,
    tags=["Регистрация"], 
    prefix="/find",
)


# app.include_router(
#     router=org_registration_router,
#     tags=["Регистрация"],
#     prefix='/account_api/register/organization',
# )


# '''
# Получение данных из БД

# '''


# app.include_router(
#     router=get_affiliation_for_register_router,
#     tags=["Получить аффилиации"],
#     prefix='/account_api/get_affiliation_for_register',
# )

# app.include_router(
#     router=get_profile_data_router,
#     tags=["Получить данные профиля пользователя"],
#     prefix='/account_api/get_profile_data',
# )

# app.include_router(
#     router=add_profile_data_router,
#     tags=["Добавить данные профиля пользователя"],
#     prefix='/account_api/add_profile_data',
# )

# app.include_router(
#     router=get_org_types_router,
#     tags=["Получить типы организации"],
#     prefix='/account_api/get_org_types',
# )

# app.include_router(
#     router=get_cities_router,
#     tags=["Получить список городов"],
#     prefix='/account_api/get_cities',
# )

# app.include_router(
#     router=get_countries_router,
#     tags=["Получить список стран"],
#     prefix='/account_api/get_countries',
# )

# app.include_router(
#     router=moderate_pages_router,
#     tags=["Модерируемые страницы"],
#     prefix='/account_api/moderate_pages',
# )

# app.include_router(
#     router=profile_header_router,
#     tags=["Шапка профиля"],
#     prefix='/account_api/profile_header',
# )


# app.include_router(
#     router=get_roles_router,
#     tags=["Названия должностей"],
#     prefix='/account_api/get_roles',
# )

# '''
# Загрузка файлов

# '''


# app.include_router(
#     router=upload_pdf_router,
#     tags=["Загрузить PDF"],
#     prefix='/account_api/upload/upload_pub',
# )

# app.include_router(
#     router=upload_correct_pdf_router,
#     tags=["Загрузить PDF"],
#     prefix='/account_api/upload/upload_correct_pub',
# )

# app.include_router(
#     router=get_upload_id_router,
#     tags=["Загрузить PDF"],
#     prefix='/account_api/upload/get_upload_id',
# )