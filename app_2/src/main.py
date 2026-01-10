from fastapi import FastAPI
from src.api.accounts_api import router as accounts_router
from src.api.goods_api import router as goods_router

app = FastAPI(title="Store API")

app.include_router(accounts_router)
app.include_router(goods_router)
