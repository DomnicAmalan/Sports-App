from pydantic import BaseModel, EmailStr, ValidationError, validator

class User(BaseModel):
    Username: str
    Firstname: str
    Lastname: str
    Password: str
    Email: EmailStr
    Mobilenumber: int

    class Config:
        orm_mode = True

class UserCreate(User):
    pass

class Login(BaseModel):
    Email: str
    Password: str
