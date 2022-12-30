from fastapi import FastAPI, HTTPException, status, Response
from sqlalchemy.orm import Session
from database.models import create_new_user, get_user_by_email
from utils import hash



def new_user(db: Session,  email:str=None, password:str=None):
    email_check = get_user_by_email(db=db, email=email)
    if email_check is not None:
            raise HTTPException(status_code=404, detail= "Email already exist!")
    else:
        hashed_password = hash(password=password)
        password = hashed_password
        data = create_new_user(db=db,email=email, password=password)
        
        return {
            "status":True,
            "message": "Success",
            "data": data
            }

