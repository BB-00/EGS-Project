from fastapi import Depends, FastAPI, Request
from fastapi.security import OAuth2PasswordRequestForm

from auth import AuthHandler
from db import DbHandler
from pydantic import BaseModel

app = FastAPI()

auth = AuthHandler()

db = DbHandler()

class UserCreate(BaseModel):
    username: str
    email: str
    password: str


@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password)

    access_token = auth.create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/register")
async def register_user(user: UserCreate):

    username = user.username
    email = user.email

    print(username)
    print(email)

    password = auth.get_password_hash(user.password)
    print(password)

    db.register_user_db(username, email, password)

    return


@app.get("/validate")
async def validate_token(token: str):
    return auth.decode_token(token)
