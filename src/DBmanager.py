from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine
from sqlalchemy.orm import declarative_base
from src.config import Config

engine = create_async_engine(
    url=Config.db_url,
    echo=True
)

session_factory = async_sessionmaker(engine, expire_on_commit=False)


async def create_all_table(model: declarative_base()):
    async with engine.begin() as connection:
        await connection.run_sync(model.metadata.create_all)


async def delete_all_table(model: declarative_base()):
    async with engine.begin() as connection:
        await connection.run_sync(model.metadata.drop_all)

base = declarative_base()
