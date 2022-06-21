from fastapi import APIRouter, status
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

from schemas.wallets import WalletCreate
from schemas.transactions import TransactionShow
from database.session import get_db
from database.repository.wallets import create_new_wallet, get_wallet#, get_walletID


router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def wallet_post(_username:str, db:Session=Depends(get_db)):
    # url = 'https://www.w3schools.com/python/demopage.php'
    # myobj = {'somekey': 'somevalue'}
    # x = requests.post(url, json = myobj)
    wallet = WalletCreate(username=_username, balance=100)
    wallet = create_new_wallet(db=db, wallet=wallet)
    return wallet

@router.get("/", response_model=List[TransactionShow])
def wallet_get(_username:str, db:Session=Depends(get_db)):
    transactions = get_wallet(db=db, username=_username)
    return transactions

# @router.get("/walletID")
# def walletID_get(_username:str, db:Session=Depends(get_db)):
#     walletID = get_walletID(db=db, username=_username)
#     return walletID