from typing import Optional
from pydantic import BaseModel

class WalletCreate(BaseModel):
    username: str
    balance: float

