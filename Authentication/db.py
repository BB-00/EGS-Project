import mariadb
import json
from pydantic import BaseModel
from typing import Union


class User(BaseModel):
    username: str
    email: Union[str, None] = None

class UserInDB(User):
    hashed_password: str


class DbHandler():

    def __init__(self):

        try:
            with open('.secret/db.json') as f:
                x = json.load(f)
                self.conn = mariadb.connect(
                    user = x['user'],
                    password = x['password'],
                    host = x['host'],
                    port = x['port'],
                    database = x['database']
                )
        except mariadb.Error as e:
            print(f"Error connecting to MariaDB Platform: {e}")
            sys.exit(1)
        
        self.cur = self.conn.cursor()


    def get_user(self, username: str):
    
        self.cur.execute("SELECT * FROM users WHERE username=?", (username,))
        
        user = self.cur.next()
        
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},)

        return UserInDB(username = user[0], email = user[1], hashed_password = user[2])


    def register_user_db(self, username: str, email: str, password: str):

        self.cur.execute("SELECT 1 FROM users WHERE username=? OR email=?", (username,email))
        x = self.cur.next()
        
        # Check if user exists and
        if x != None and x[0] == 1:
            raise HTTPException(status_code=401, detail='Email or Username already in use')
        else:
            try: 
                self.cur.execute("INSERT INTO users (username,email,password) VALUES (?,?,?)", (username,email,password))
                self.conn.commit()
            except mariadb.Error as e: 
                print(f"Error: {e}")
