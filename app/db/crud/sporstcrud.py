from sqlalchemy.orm import Session

from ..models import sportsmodel
from ..schemas import sports_schema


def create_sports_list(db: Session, data):
    sports_list = sportsmodel.Sports(**data)
    db.merge(sports_list)
    db.commit()
    return data
