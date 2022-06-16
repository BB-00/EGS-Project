from datetime import datetime, timedelta
from typing import Union

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel

from auth import AuthHandler
from db import DbHandler
import json
import mariadb
import sys


app = FastAPI()

auth = AuthHandler()

db = DbHandler()


@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = auth.authenticate_user(form_data.username, form_data.password)

    access_token = auth.create_access_token(data={"sub": user.username})

    return {"access_token": access_token, "token_type": "bearer"}


@app.post("/register")
async def register_user(username: str, email: str, password: str):

    password = auth.get_password_hash(password);

    db.register_user_db(username, email, password)

    return


@app.get("/validate")
async def validate_token(token: str, ):
    return auth.decode_token(token)
