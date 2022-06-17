from fastapi import FastAPI
from apis.base import api_router
from database.session import engine
from database.base import Base

def include_router(app):
	app.include_router(api_router)

def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title="PaymentsAPI", version=1)
    include_router(app)
    create_tables()
    return app

app = start_application()