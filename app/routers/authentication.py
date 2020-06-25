from fastapi import APIRouter, Depends, HTTPException, Response, status
from fastapi.responses import JSONResponse
from ..handlers import email
from sqlalchemy.orm import Session

from ..db.schemas import users_schema
from ..db.models import usermodel
from ..db.crud import usercrud
from ..db.database import SessionLocal, engine
from ..db.connect_db import get_db

authenticate = APIRouter()

usermodel.Base.metadata.create_all(bind=engine)

@authenticate.post("/register", tags=["users"])
async def create_user(user: users_schema.User, db: Session = Depends(get_db)):
    exists = usercrud.check_email_mobile_exists(db,Email=user.Email, Mobilenumber=user.Mobilenumber)
    if email.check_mail(user.Email):
        if exists:
            return JSONResponse(status_code=409, content="Username already registered")
        created = usercrud.create_user(db=db, user=user)
        if created:
            if email.check_mail(user.Email):
                await email.send_email(user.Email)
            else:
                JSONResponse(status_code=409, content="Username already registered")
        return JSONResponse(status_code=200, content=created)
    else:
        return JSONResponse(status_code=422, content="Invalid Email Address")

@authenticate.get('/check-username/{username}', tags=["users"])
async def check_username(username: str, db: Session = Depends(get_db)):
    exists = usercrud.check_username_exists(db,Username=username)
    if exists:
        return JSONResponse(status_code=409, content=False)
    return JSONResponse(status_code=200, content=True)

@authenticate.post('/login', tags=["users"])
async def login(Login: users_schema.Login, db:Session = Depends(get_db)):
    verified = usercrud.login_check(db, Email=Login.Email, Password=Login.Password)
    if verified:
        if verified == "No User Found":
            return JSONResponse(status_code=404, content=verified)
        return JSONResponse(status_code=200, content=verified)
    return JSONResponse(status_code=401, content=verified)

