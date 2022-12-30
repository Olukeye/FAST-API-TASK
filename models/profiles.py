from sqlalchemy import Column, BigInteger, Integer, Boolean, String, ForeignKey, func, desc
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from typing import  Optional
from database.db import  Base, get_db, create_customised_datetime
from typing import Dict
from models.users import User


class Profile(Base):
    __tablename__ = "profiles"
    id = Column(Integer, primary_key=True, nullable=False)
    username = Column(String, unique=True, nullable=True)
    bio = Column(String, nullable=True)
    followers = Column(Boolean, server_default='TRUE', nullable=False)
    created_at = Column(String, nullable=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    user = relationship("User")



def create_new_profile(db:Session,user:int=0, username:str=None, bio:str=None, followers:str=None):
    new_profile = Profile(username=username, bio=bio, followers=followers, created_at=create_customised_datetime(), user=user)
    
    db.add(new_profile)
    db.commit()
    db.refresh(new_profile)
  
    
    return new_profile


def search_query(db: Session, user=int, limit:int = 9, skip:int=0, search:Optional[str] = ""):
    return db.query(Profile, func.count(Profile.followers).label("followers")).group_by(Profile.id).filter(Profile.username.contains(search)).limit(limit).offset(skip).all()
    