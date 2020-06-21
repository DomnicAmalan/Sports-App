from fastapi import APIRouter, Depends, HTTPException, Response
from fastapi.responses import JSONResponse
from ..handlers import email

authenticate = APIRouter()

from sqlalchemy.orm import Session

from ..db.schemas import users_schema
from ..db.models import usermodel
from ..db.crud import usercrud
from ..db.database import SessionLocal, engine

usermodel.Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@authenticate.post("/register", tags=["users"], response_model=users_schema.User)
async def create_user(user: users_schema.UserCreate, db: Session = Depends(get_db)):
    exists = usercrud.check_email_mobile_exists(db,Email=user.Email, Mobilenumber=user.Mobilenumber)
    if exists:
        return JSONResponse(status_code=409, content="Username already registered")
    created = usercrud.create_user(db=db, user=user)
    if created:
        await email.send_email(user.Email)
    return created

@authenticate.get('/check-username/{username}', tags=["users"])
async def check_username(username: str, db: Session = Depends(get_db)):
    exists = usercrud.check_username_exists(db,Username=username)
    if exists:
        return JSONResponse(status_code=409, content=True)
    return JSONResponse(status_code=200, content=False)

@authenticate.post('/login', tags=["users"])
async def login(Login: users_schema.Login, db:Session = Depends(get_db)):
    exists = usercrud.login_check(db, Email=Login.Email, Password=Login.Password)
    if exists:
        return JSONResponse(status_code=200, content=True)
    return JSONResponse(status_code=401, content=False)


