from fastapi import APIRouter, HTTPException
from sqlalchemy.future import select
from src.models.accounts import Accounts
from src.models.base import async_session

router = APIRouter(prefix="/accounts", tags=["Accounts"])

#* Создаёт аккаунт
@router.post("/")
async def create_account(item: dict):
    async with async_session() as session:
        acc = Accounts(**item)
        session.add(acc)
        await session.commit()
        return {"status": "created", "account": item}

#* Получить аккаунт по id_accounts
@router.get("/{id_accounts}")
async def get_account(id_accounts: int):
    async with async_session() as session:
        result = await session.execute(
            select(Accounts).where(Accounts.id_accounts == id_accounts)
        )
        acc = result.scalar_one_or_none()
        if not acc:
            raise HTTPException(status_code=404, detail="Account not found")
        return acc


#* Обновить аккаунт
@router.put("/{id_accounts}")
async def update_account(id_accounts: int, data: dict):
    async with async_session() as session:
        result = await session.execute(
            select(Accounts).where(Accounts.id_accounts == id_accounts)
        )
        acc = result.scalar_one_or_none()
        if not acc:
            raise HTTPException(status_code=404, detail="Account not found")
        for key, value in data.items():
            setattr(acc, key, value)
        await session.commit()
        return {"status": "updated"}

#* Удаляет аккаунт
@router.delete("/{id_accounts}")
async def delete_account(id_accounts: int):
    async with async_session() as session:
        result = await session.execute(
            select(Accounts).where(Accounts.id_accounts == id_accounts)
        )
        acc = result.scalar_one_or_none()
        if not acc:
            raise HTTPException(status_code=404, detail="Account not found")
        await session.delete(acc)
        await session.commit()
        return {"status": "deleted"}
