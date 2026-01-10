from sqlalchemy import Column, Integer, String, Float
from src.models.base import Base

class Goods(Base):
    __tablename__ = "goods"

    id_goods = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)
    description = Column(String)
    image = Column(String)
