from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from typing import  List, Optional
from sqlalchemy.orm import Session
from modules.profiles import new_profile, search
from schemas.profiles import CreateProfileModel, ProfileOption
from schemas.response_models import ResponseModel
from database.db import get_db
from oauth2 import get_current_user

router = APIRouter(tags = ['Profiles'])


@router.post("/profiles",  status_code=201,response_model=ResponseModel)
def create_profile(field:CreateProfileModel, user:int= Depends(get_current_user), db: Session=Depends(get_db)):
    return new_profile(db=db, user=user, username=field.username, bio=field.bio, followers=field.followers)



@router.get("/search",  status_code=200, response_model=ResponseModel)
def search_profile(user:int= Depends(get_current_user),  db: Session=Depends(get_db)):
    return search(db=db, user=user)