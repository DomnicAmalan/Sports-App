from ..db.database import SessionLocal, engine
from sqlalchemy.orm import Session
from ..db.models import usermodel, sportsmodel

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()