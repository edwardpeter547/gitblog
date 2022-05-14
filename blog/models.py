from sqlalchemy import Integer, String, DateTime, Float, Column
from datetime import datetime
from .database import Base, engine, session_local

class User():
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String)
    mobile = Column(String)
    datecreated = Column(DateTime, default = datetime.utcnow, nullable=False)
    
    
class Blog():
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    datecreated = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    
class Category():
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    catname = Column(String)
    datecreated = Column(DateTime, default=datetime.utcnow, nullable=False)
    