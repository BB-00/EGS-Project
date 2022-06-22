from fastapi import APIRouter, status
from fastapi import Request
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List
from fastapi.templating import Jinja2Templates

from schemas.wallets import WalletCreate
# from schemas.transactions import TransactionShow
from database.session import get_db
from database.repository.wallets import create_new_wallet, get_wallet
from database.repository.transactions import get_transactions

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.post("/", status_code=status.HTTP_201_CREATED)
def wallet_post(_username:str, db:Session=Depends(get_db)):
    wallet = WalletCreate(username=_username, balance=100)
    wallet = create_new_wallet(db=db, wallet=wallet)
    return wallet

@router.get("/")
async def wallet_get(request: Request, _username:str, db:Session=Depends(get_db)):
    wallet = get_wallet(db=db, username=_username)
    transactions = get_transactions(db=db, walletID=wallet.walletID)
    return templates.TemplateResponse("general_pages/homepage.html",{"request":request, "transactions":transactions})
