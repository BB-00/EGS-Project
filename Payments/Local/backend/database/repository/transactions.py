from datetime import datetime
from sqlalchemy.orm import Session
from typing import Union

from schemas.transactions import TransactionCreate
from database.models.transactions import Transactions

def create_new_transaction(transaction:TransactionCreate, db:Session):
    transaction = Transactions(amount=transaction.amount,
        methodID=transaction.methodID,
        walletID=transaction.walletID)
    db.add(transaction)
    db.commit()
    db.refresh(transaction)
    return transaction

def get_transactions(db:Session, walletID:int, offset:Union[int,None]=None, limit:Union[int,None]=None, amount:Union[int,None]=None, date_begin: Union[datetime,None]=None, date_end: Union[datetime,None]=None):
    if amount is None and date_begin is None and date_end is None:
        return db.query(Transactions).filter(Transactions.walletID == walletID).offset(offset).limit(limit).all()
    if amount is not None and date_begin is None and date_end is None:
        return db.query(Transactions).filter(Transactions.amount == amount, Transactions.walletID == walletID).offset(offset).limit(limit).all()
    if amount is None and date_begin is not None and date_end is not None:
        return db.query(Transactions).filter(Transactions.date >= date_begin, Transactions.date <= date_end, Transactions.walletID == walletID).offset(offset).limit(limit).all()
    if amount is None and date_begin is not None and date_end is None:
        return db.query(Transactions).filter(Transactions.date >= date_begin, Transactions.walletID == walletID).offset(offset).limit(limit).all()
    if amount is None and date_begin is None and date_end is not None:
        return db.query(Transactions).filter(Transactions.date <= date_end, Transactions.walletID == walletID).offset(offset).limit(limit).all()
    if amount is not None and date_begin is not None and date_end is not None:
        return db.query(Transactions).filter(Transactions.amount == amount, Transactions.date >= date_begin, Transactions.date <= date_end, Transactions.walletID == walletID).offset(offset).limit(limit).all()

def get_transaction(db:Session, transactionID:int):
    return db.query(Transactions).filter(Transactions.transactionID == transactionID).all()