from fastapi import FastAPI
from apis.base import api_router
from database.session import engine
from database.base import Base
from fastapi.staticfiles import StaticFiles

def include_router(app):
	app.include_router(api_router)

def configure_static(app):
    app.mount("/static", StaticFiles(directory="static"), name="static")

def create_tables():
    print("create_tables")
    Base.metadata.create_all(bind=engine)

def start_application():
    app = FastAPI(title="PaymentsAPI", version=1)
    include_router(app)
    configure_static(app)
    create_tables()
    return app

app = start_application()