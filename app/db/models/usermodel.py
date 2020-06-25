from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,BigInteger, DateTime
from sqlalchemy.orm import relationship

from ..database import Base
from datetime import datetime


class User(Base):
    __tablename__ = "users"
    Email = Column(String, primary_key=True, unique=True, index=True)
    Firstname = Column(String, index=True)
    Lastname = Column(String, index=True)
    Password = Column(String)
    Mobilenumber =  Column(BigInteger, index=True, unique=True)
    Username = Column(String, index=True, unique=True)
    CreatedDate = Column(DateTime,default=datetime.utcnow)
    UpdatedDate = Column(DateTime,default=datetime.utcnow)