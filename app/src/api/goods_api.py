from fastapi import APIRouter, HTTPException
from sqlalchemy.future import select
from src.models.goods import Goods
from src.models.base import async_session

router = APIRouter(prefix="/goods", tags=["Goods"])

#*Создать новый товар
@router.post("/")
async def create_good(item: dict):
    async with async_session() as session:
        good = Goods(**item)
        session.add(good)
        await session.commit()
        await session.refresh(good)
        return {"status": "created", "good": good.__dict__}

#*Получить товар по id_goods
@router.get("/{id_goods}")
async def get_good(id_goods: int):
    async with async_session() as session:
        result = await session.execute(
            select(Goods).where(Goods.id_goods == id_goods)
        )
        good = result.scalar_one_or_none()
        if not good:
            raise HTTPException(status_code=404, detail="Good not found")
        return good.__dict__

#* Обновить товар
@router.put("/{id_goods}")
async def update_good(id_goods: int, data: dict):
    async with async_session() as session:
        result = await session.execute(
            select(Goods).where(Goods.id_goods == id_goods)
        )
        good = result.scalar_one_or_none()
        if not good:
            raise HTTPException(status_code=404, detail="Good not found")
        for key, value in data.items():
            setattr(good, key, value)
        await session.commit()
        return {"status": "updated"}

#*Удалить товар
@router.delete("/{id_goods}")
async def delete_good(id_goods: int):
    async with async_session() as session:
        result = await session.execute(
            select(Goods).where(Goods.id_goods == id_goods)
        )
        good = result.scalar_one_or_none()
        if not good:
            raise HTTPException(status_code=404, detail="Good not found")
        await session.delete(good)
        await session.commit()
        return {"status": "deleted"}
