from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from fastapi import HTTPException
from db import DbHandler
import json


with open('.secret/key.json') as f:
    x = json.load(f)

SECRET_KEY = x['KEY']
ALGORITHM = x['ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = x['ACCESS_TOKEN_EXPIRE_MINUTES']


class AuthHandler():

    pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

    oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

    db = DbHandler()


    def create_access_token(self, data, expires_delta=None):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt


    def decode_token(self, token):
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return payload['sub']
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature Expired')
        except jwt.JWTError:
            raise HTTPException(status_code=401, detail='Invalid Token')


    def authenticate_user(self, username, password):
        user = self.db.get_user(username)

        if not self.verify_password(password, user.hashed_password):
            return False
        return user


    def verify_password(self, plain_password, hashed_password):
        return self.pwd_context.verify(plain_password, hashed_password)


    def get_password_hash(self, password):
        return self.pwd_context.hash(password)
