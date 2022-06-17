from sqlalchemy import Column, Integer, Float, String

from database.base_class import Base

class Wallets(Base):
    __tablename__ = 'Wallets'
    walletID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    username = Column(String(50), nullable=False)
    balance = Column(Float, nullable=False)
