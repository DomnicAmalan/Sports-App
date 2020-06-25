from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,BigInteger, UnicodeText, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class Sports(Base):
    __tablename__ = "sportslist"
    Id = Column(Integer, primary_key=True, unique=True)
    Name = Column(String, index=True)
    Description = Column(UnicodeText, index=True)
    Slug = Column(String)
    Tags = Column(String)
    GroupID = Column(Integer)
    CreatedDate = Column(DateTime,default=datetime.utcnow, nullable=True)
    UpdatedDate = Column(DateTime,default=datetime.utcnow)

class SportRelationship(Base):
    __tablename__ = "sportsrelation"
    Id = Column(Integer, primary_key=True, unique=True)
    SubSportIDs = Column(String)
    RelatedSportIDs = Column(String)
    ImageLinks = Column(String)
    CreatedDate = Column(DateTime,default=datetime.utcnow)
    UpdatedDate = Column(DateTime,default=datetime.utcnow)
    parent_id = Column(Integer, ForeignKey('sportslist.Id'))