from sqlalchemy import Column, Integer, String
from src.models.base import Base

class Accounts(Base):
    __tablename__ = "accounts"

    id_accounts = Column(Integer, primary_key=True, index=True)
    familiya = Column(String)               # <-- исправлено
    name = Column(String)
    otchestvo = Column(String)
    adress = Column(String)
    years = Column(Integer)
    email = Column(String, unique=True)
    user_number = Column(Integer, unique=True)
    password = Column(String)
    user_like = Column(Integer)          # <-- "like" в кавычках, т.к. SQL-ключевое слово
