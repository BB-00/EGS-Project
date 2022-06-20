from fastapi import APIRouter
from apis.version1 import route_general_pages
from apis.version1 import route_addFunds
from apis.version1 import route_transactions
from apis.version1 import route_wallets

api_router = APIRouter()
api_router.include_router(route_general_pages.general_pages_router, prefix="/payments", tags=["payments"])
api_router.include_router(route_addFunds.router, prefix="/addFunds", tags=["addFunds"])
api_router.include_router(route_transactions.router, prefix="/transactions", tags=["transactions"])
api_router.include_router(route_wallets.router, prefix="/wallets", tags=["wallets"])
