from fastapi import FastAPI
import uvicorn
from src.item_storage.router import router as item_storage_router
from utils import life_span
from src.auth.router import router as auth_router

app = FastAPI(lifespan=life_span)

@app.get("/", tags=["root"])
async def root():
    return {"Hello": "World"}

app.include_router(item_storage_router)
app.include_router(auth_router)


if __name__ == "__main__":
    uvicorn.run(
                    app,
                    host="0.0.0.0",
                    port=8000
                )