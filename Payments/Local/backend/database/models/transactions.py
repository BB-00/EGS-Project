from sqlalchemy import Column, Integer, Float, ForeignKey, TIMESTAMP
from sqlalchemy import text

from database.base_class import Base

class Transactions(Base):
    __tablename__ = 'Transactions'
    transactionID = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    amount = Column(Float, nullable=False)
    methodID = Column(Integer, nullable=False)
    date = Column(TIMESTAMP, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=False)
    walletID = Column(Integer, ForeignKey('Wallets.walletID'), nullable=False)
