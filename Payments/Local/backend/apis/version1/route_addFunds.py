from fastapi import APIRouter, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import Depends

from schemas.transactions import TransactionCreate
from database.session import get_db
from database.repository.transactions import create_new_transaction, get_transactions
from database.models.wallets import Wallets

router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def add_funds_post(transaction: TransactionCreate, db:Session=Depends(get_db)):
    if transaction.amount < 0:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="add funds: amount needs to be higher than 0!"
        )
    if transaction.methodID not in [0, 1, 2]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="add funds: method of payment is wrong!"
        )
    if db.query(Wallets).filter(Wallets.walletID == transaction.walletID).first() == None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="add funds: wallet is not valid!"
        )
    transaction = create_new_transaction(transaction=transaction, db=db)
    return transaction
