from fastapi import FastAPI

from src.wildberries.router import router as wildberries_router


app = FastAPI()
app.include_router(wildberries_router)