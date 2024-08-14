from fastapi import FastAPI
import uvicorn
from contextlib import asynccontextmanager
from DBmanager import create_all_table, delete_all_table
from DBmanager import base
from src.item_storage.router import router as item_storage_router

@asynccontextmanager
async def life_span(app: FastAPI):
    await delete_all_table(base)
    await create_all_table(base)
    print("Base was created")
    yield

app = FastAPI(lifespan=life_span)


@app.get("/")
async def root():
    return {"Hello": "World"}

app.include_router(item_storage_router)

if __name__ == "__main__":
    uvicorn.run(
                    app,
                    host="0.0.0.0",
                    port=8000
                )