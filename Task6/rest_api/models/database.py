from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
import asyncio
from sqlalchemy import text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
#from urllib.parse import quote_plus

#encoded_password = quote_plus("sf3dvxQFWq@!")
SQLALCHEMY_DATABASE_URL = "postgresql+asyncpg://postgres:123103Pp@host.docker.internal:5432/mai_arch_db"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

Base = declarative_base()

# async def init_db():
#     async with engine.begin() as conn:
#         # Синхронно создаем все таблицы
#         await conn.run_sync(Base.metadata.create_all)

# async def test_connection():
#     try:
#         # Проверка подключения
#         async with engine.connect() as conn:
#             result = await conn.execute(text("SELECT 1"))
#             print("Connection successful, result:", result.scalar_one())
#     except Exception as e:
#         print(f"Connection failed: {e}")

# # Запуск асинхронной функции
# asyncio.run(test_connection())