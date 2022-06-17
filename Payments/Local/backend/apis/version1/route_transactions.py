from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import Union
from datetime import datetime
from typing import List

from schemas.transactions import TransactionCreate, TransactionShow
from database.session import get_db
from database.repository.transactions import create_new_transaction, get_transactions, get_transaction
import database.models.wallets as wallets

router = APIRouter()

@router.get("/", response_model=List[TransactionShow], status_code=status.HTTP_200_OK)
def transaction_get(_walletID:int, db:Session=Depends(get_db), _offset: Union[int,None]=None, _limit: Union[int,None]=None, _amount: Union[int,None]=None, _date_begin: Union[datetime,None]=None, _date_end: Union[datetime,None]=None):
    list_transactions = get_transactions(db=db, walletID=_walletID, offset=_offset, limit=_limit, amount=_amount, date_begin=_date_begin, date_end=_date_end)
    return list_transactions

@router.post("/", status_code=status.HTTP_201_CREATED)
def transaction_post(transaction: TransactionCreate, db:Session=Depends(get_db)):
    if transaction.amount > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="transactions: amount needs to be lower than 0!"
        )
    if transaction.methodID not in [0, 1, 2]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="transactions: method of payment is wrong!"
        )
    if db.query(wallets.Wallets).filter(wallets.Wallets.walletID == transaction.walletID).first() == None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="transactions: wallet is not valid!"
        )
    transaction = create_new_transaction(db=db, transaction=transaction)
    return transaction

@router.get("/{transaction_id}", response_model=TransactionShow, status_code=status.HTTP_200_OK)
def transaction_transaction_id_get(transaction_id:int, db:Session=Depends(get_db)):
    transaction = get_transaction(db=db, transactionID=transaction_id)
    if len(transaction) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="transaction: id does not exist"
        )
    return transaction

@router.post("/{transaction_id}/refund", status_code=status.HTTP_201_CREATED)
def transaction_transaction_id_refund_post(transaction_id: int, db:Session=Depends(get_db)):
    transaction = get_transaction(db=db, transactionID=transaction_id)
    if len(transaction) == 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="transaction: id does not exist"
        )
    transaction[0].amount = -transaction[0].amount
    transaction[0] = create_new_transaction(db=db, transaction=transaction[0])
    return transaction[0]
