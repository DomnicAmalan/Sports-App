from fastapi import Depends, FastAPI, Header, HTTPException
from app.routers import authentication, sports, locations
from sqlalchemy.orm import Session

from .db.database import SessionLocal, engine

# models.Base.metadata.create_all(bind=engine)
app = FastAPI()


# async def get_token_header(x_token: str = Header(...)):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.include_router(
    authentication.authenticate,
    prefix="/authenticate",
    tags=["authentication"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    sports.sports,
    prefix="/sports",
    tags=["sports"],
    responses={404: {"description": "Not found"}},
)

app.include_router(
    locations.locations,
    prefix="/location",
    tags=["location"],
    responses={404: {"description": "Not found"}}
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)