from fastapi import FastAPI
from src.api.accounts_api import router as accounts_router

app_1 = FastAPI(title="Store API")

app_1.include_router(accounts_router)

