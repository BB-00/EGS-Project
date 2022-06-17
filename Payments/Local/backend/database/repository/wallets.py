from sqlalchemy.orm import Session

from schemas.wallets import WalletCreate
from database.models.wallets import Wallets

def create_new_wallet(wallet:WalletCreate, db:Session):
    wallet = Wallets(username=wallet.username,
        balance=wallet.balance)
    db.add(wallet)
    db.commit()
    db.refresh(wallet)
    return wallet

def get_wallet(db:Session, username:str):
    wallet = db.query(Wallets).filter(Wallets.username == username).all()
    return wallet