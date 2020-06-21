from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,BigInteger
from sqlalchemy.orm import relationship

from ..database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, autoincrement=True)
    Email = Column(String, unique=True, index=True)
    Firstname = Column(String, index=True)
    Lastname = Column(String, index=True)
    Password = Column(String)
    Mobilenumber =  Column(BigInteger, index=True, unique=True)
    Username = Column(String, index=True, unique=True)