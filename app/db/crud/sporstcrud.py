from sqlalchemy.orm import Session

from ..models import sportsmodel
from ..schemas import sports_schema
from ...helpers import encrypt
from sqlalchemy.dialects.postgresql import insert
import pickle


def create_sports_list(db: Session, data):
    sports_list = sportsmodel.Sports(**data)
    db.merge(sports_list)
    db.commit()
    return data
