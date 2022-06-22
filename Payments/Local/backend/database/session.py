import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator


with open('.secret/key_db.json') as f:
    x = json.load(f)
    engine = create_engine(x['url'], echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Generator:
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()