from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
import requests
from ..db.schemas import location_schema
from ..db.models import locationmodel
from ..db.crud import locationcrud
from sqlalchemy.orm import Session
from ..db.connect_db import get_db
from ..db.database import SessionLocal, engine

locations = APIRouter()

locationmodel.Base.metadata.create_all(bind=engine)

@locations.post('/store-location', tags=['location'])
def location_detect_store(location: location_schema.Location, db:Session = Depends(get_db)):
    request_data = requests.get("https://api.bigdatacloud.net/data/reverse-geocode-client?latitude={0}&longitude={1}&localityLanguage=en".format(location.Latitude, location.Longitude))
    data = request_data.json()
    prepared = dict(
        Email= location.Email,
        Latitude= location.Latitude,
        Longitude= location.Longitude,
        Continent= data["continent"] if data["continent"] else None,
        ContinentCode= data["continentCode"] if data["continentCode"] else None,
        CountryName= data["countryName"] if data["countryName"] else None,
        CountryCode= data["countryCode"] if data["countryCode"] else None,
        PrincipalSubdivision= data["principalSubdivision"] if data["principalSubdivision"] else None,
        PrincipalSubdivisionCode = data["principalSubdivisionCode"] if data["principalSubdivisionCode"] else None,
        City= data["city"] if data["city"] else None,
        Locality= data["locality"] if data["locality"] else None,
        PostCode= data["postcode"] if data["postcode"] else None
    )
    location = prepared
    result = locationcrud.store_analytics_location(db, location)

    return JSONResponse(status_code=200, content=request_data.json())