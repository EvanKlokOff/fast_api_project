from fastapi import FastAPI
from contextlib import asynccontextmanager
from src.DBmanager import create_all_table, delete_all_table
from src.DBmanager import base


@asynccontextmanager
async def life_span(app: FastAPI):
    await delete_all_table(base)
    await create_all_table(base)
    print("Base was created")
    yield