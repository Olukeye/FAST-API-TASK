from fastapi import FastAPI, HTTPException, status, Response
from sqlalchemy.orm import Session
from database.models import create_new_profile, search_query


def new_profile(db:Session, user:int=0, username:str=None, bio:str=None, followers:str=None):
    data = create_new_profile(db=db, username=username, bio=bio, followers=followers, user=user)
    
    return {
        "status":True,
        "message":"Success",
        "data": data
    }
    
def search(db: Session, user:int):
    data = search_query(db=db)
     
    return {
        "status":True,
        "message":"Success",
        "data": data
    }