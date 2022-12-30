from pydantic import BaseModel,EmailStr, constr
from typing import Optional

class User(BaseModel):
    email: str
    password:str
    created_at: Optional[str]= None
 
class CreateUserModel(User):
     pass
 
 
class UserOption(BaseModel):
    id:int
    username: str
    email: str
  
    class Config:
        orm_mode = True
  