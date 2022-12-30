from sqlalchemy import Column, BigInteger, Integer, Boolean, String
from sqlalchemy.sql.expression import text
from sqlalchemy.orm import Session
from database.db import Base, get_db, create_customised_datetime


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(String, nullable=False)


def get_user_by_email(db: Session, email: str=None):
    return db.query(User).filter(User.email == email).first()

def create_new_user(db:Session,  email:str=None, password:str=None):
    new_user = User(email=email, password=password,created_at=create_customised_datetime())
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user
