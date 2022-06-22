from fastapi import APIRouter, HTTPException, status, Form
from fastapi import Depends
from fastapi.responses import RedirectResponse
from sqlalchemy.orm import Session
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

@router.post("/")
def transaction_post(_amount: str=Form(), _methodID: str=Form(), _username: str=Form(), db:Session=Depends(get_db)):
    _walletID = db.query(wallets.Wallets.walletID).filter(wallets.Wallets.username == _username).one()
    _walletID = _walletID[0]
    if _walletID is None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="transactions: wallet is not valid!"
        )
    if - float(_amount) > 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="transactions: amount needs to be lower than 0!"
        )
    if int(_methodID) not in [0, 1, 2]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="transactions: method of payment is wrong!"
        )
    transaction = TransactionCreate(amount= - float(_amount), methodID=int(_methodID), walletID=int(_walletID))
    transaction = create_new_transaction(db=db, transaction=transaction)
    return RedirectResponse("http://127.0.0.1:5000/payment_successfull")

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
