from sqlalchemy.orm import Session
from ..models import locationmodel

def store_analytics_location(db: Session, data):
    location = locationmodel.Location(**data)
    db.merge(location)
    db.commit()
    return data
    return data
