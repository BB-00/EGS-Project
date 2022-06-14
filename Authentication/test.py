from datetime import datetime, timedelta

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import JWTError, jwt
from passlib.context import CryptContext
from pydantic import BaseModel
import json
import mariadb
import sys

with open('.secret/key.json') as f:
    x = json.load(f)

SECRET_KEY = x["KEY"]
ALGORITHM = x['ALGORITHM']
ACCESS_TOKEN_EXPIRE_MINUTES = x['ACCESS_TOKEN_EXPIRE_MINUTES']


######## Database Connection #########


try:
    with open('.secret/db.json') as f:
        x = json.load(f)
        conn = mariadb.connect(
            user = x['user'],
            password = x['password'],
            host = x['host'],
            port = x['port'],
            database = x['database']
        )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

cur = conn.cursor()


###################


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Union[str, None] = None


class User(BaseModel):
    username: str
    email: Union[str, None] = None


class UserInDB(User):
    hashed_password: str



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def get_password_hash(password):
    return pwd_context.hash(password)



def get_user(cur_db, username: str):
    
    cur_db.execute("SELECT * FROM users WHERE username=?", (username,))
    
    user = cur.next()
    
    if user is None:
        raise credentials_exception

    return UserInDB(username = user[0], email = user[1], hashed_password = user[2])



def authenticate_user(cur_db, username: str, password: str):
    user = get_user(cur_db, username)

    if not verify_password(password, user.hashed_password):
        return False
    return user



def create_access_token(data: dict, expires_delta: Union[timedelta, None] = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# FAZER ESTE AQUI COM A BASE DE DADOS
@app.post("/token")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    user = authenticate_user(cur, form_data.username, form_data.password)
    
    if not user:
        raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Incorrect username or password",
        headers={"WWW-Authenticate": "Bearer"},
    )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    
    try:
        cur.execute("INSERT INTO tokens (username,token) VALUES (?,?)", (user.username,access_token))
        conn.commit()
    except mariadb.Error as e:
        print(f"Error: {e}")

    return {"access_token": access_token, "token_type": "bearer"}



@app.post("/register")
async def register_user(username: str, email: str, password: str):

    cur.execute("SELECT 1 FROM users WHERE username=? OR email=?", (username,email))
    x = cur.next()
    
    # Check if user exists and
    if x != None and x[0] == 1:
        raise HTTPException(status_code=401, detail='Email or username already in use')
    else:
        try: 
            cur.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)", (username,email,get_password_hash(password),0))
            conn.commit()
        except mariadb.Error as e: 
            print(f"Error: {e}")

    return



@app.get("/validate")
async def validate_token(token: str, ):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Signature Expired')
    except jwt.JWTError:
        raise HTTPException(status_code=401, detail='Invalid Token')

