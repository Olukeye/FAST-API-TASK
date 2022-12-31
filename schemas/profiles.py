from pydantic import BaseModel,EmailStr, constr
from typing import Optional

class Profile(BaseModel):
    username: Optional[str]= None
    bio :Optional[str]= None
    followers: bool = True
    
 
class CreateProfileModel(Profile):
     pass
 