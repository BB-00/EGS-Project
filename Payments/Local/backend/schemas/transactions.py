from pydantic import BaseModel

class TransactionCreate(BaseModel):
    amount: float
    methodID: int
    walletID: int

class TransactionShow(BaseModel):
    transactionID: int
    amount: float
    methodID: int
    date: str
    walletID: int
