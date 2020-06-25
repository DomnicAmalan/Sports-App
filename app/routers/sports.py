from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from ..db.schemas import sports_schema
from ..db.crud import sporstcrud
import requests, json
from sqlalchemy.orm import Session
from ..db.connect_db import get_db
from ..db.models import sportsmodel

sports = APIRouter()

@sports.get('/refresh/sportslist', tags=['sports'])
async def sports_refresh(sports: sports_schema.Sports, db:Session = Depends(get_db)):
    request_sport = requests.get("https://sports.api.decathlon.com/sports")
    try:
        if request_sport:
            sports_data = request_sport.json()
            final_data = []
            for sport in sports_data["data"]:
                db_data = {
                            "Id": sport["id"], 
                            "Name": sport["attributes"]["name"], 
                            "Description": sport["attributes"]["description"], 
                            "Slug": sport["attributes"]["slug"], 
                            "GroupID": sport["relationships"]["group"]["data"]["id"] if "id" in sport["relationships"]["group"]["data"] else db_data.pop("GroupID"),
                            "Tags": ",".join([i for i in sport["relationships"]["tags"]["data"]])
                        }
                sports = db_data

                result = sporstcrud.create_sports_list(db, sports)
                final_data.append(result['Id'])
            return JSONResponse(status_code=200, content=json.dumps(final_data))
    except Exception as e:
        return JSONResponse(status_code=417, content="Code Error")
    else:
        return JSONResponse(status_code=417, content="Decathalon Api Failed")
