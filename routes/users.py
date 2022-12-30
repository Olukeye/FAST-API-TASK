from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter, Request
from typing import  List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from modules.users import new_user
from schemas.users import CreateUserModel
from schemas.response_models import ResponseModel
from database.db import get_db

router = APIRouter(tags = ['Users'])



@router.post("/user", status_code=201,response_model=ResponseModel)
async def create_account(fields:CreateUserModel, db: Session=Depends(get_db)):
    return new_user(db=db,email=fields.email, password=fields.password)

