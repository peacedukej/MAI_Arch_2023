from rest_api.models.database import SessionLocal, engine, Base
from sqlalchemy.ext.asyncio import AsyncSession

async def get_db(): 
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)
    db = SessionLocal() 
    try: 
        yield db 
    finally: 
        await db.close()

# async def get_db():
#     async with SessionLocal() as session:
#         try:
#             yield session
#         finally:
#             await session.close()


# async def get_db():
#     async with SessionLocal() as session:
#         yield session