from pydantic import BaseModel,EmailStr, constr
from typing import Optional

class Profile(BaseModel):
    username: Optional[str]= None
    bio :Optional[str]= None
    followers: bool = True
    
 
class CreateProfileModel(Profile):
     pass
 
 
class ProfileOption(BaseModel):
    id:int
    username: str
    bio :str
    followers:str
  
    class Config:
        orm_mode = True
  