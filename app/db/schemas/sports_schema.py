from pydantic import BaseModel, EmailStr, ValidationError, validator

class Sports(BaseModel):
    Id = int
    Name = str
    Description = str
    Slug = str
    Tags = str
    GroupIDs = str
    CreatedDate = str
    UpdatedDate = str

    class Config:
        orm_mode = True

class SportsRefresh(Sports):
    pass

class SportsRelation(BaseModel):
    SubSportIDs = str
    RelatedSportIDs = str
    ImageLinks = str
