from sqlalchemy import Boolean, Column, ForeignKey, Integer, String,BigInteger, UnicodeText, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from ..database import Base


class Location(Base):
    __tablename__ = "location_analytics"
    Id= Column(Integer, autoincrement=True, unique=True)
    Email= Column(String, primary_key=True, unique=True, index=True)
    Latitude= Column(String)
    Longitude= Column(String)
    Continent= Column(String, index=True)
    ContinentCode= Column(String, index=True)
    CountryName= Column(String, index=True)
    CountryCode= Column(String, index=True)
    PrincipalSubdivision= Column(String, index=True)
    City= Column(String, index=True)
    Locality= Column(String, index=True)
    PostCode= Column(Integer, index=True)
    PrincipalSubdivisionCode= Column(String, index=True)
    CreatedDate = Column(DateTime,default=datetime.utcnow, nullable=True)
    UpdatedDate = Column(DateTime,default=datetime.utcnow)