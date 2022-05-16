from sqlalchemy import Integer, String, DateTime, Float, Column
from datetime import datetime
from .database import Base, engine, session_local

class User(Base):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String)
    email = Column(String)
    mobile = Column(String)
    password = Column(String, nullable=False)
    datecreated = Column(DateTime, default = datetime.utcnow, nullable=False)
    
    
class Blog(Base):
    __tablename__ = "blog"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    content = Column(String)
    datecreated = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    
class Category(Base):
    __tablename__ = "category"
    id = Column(Integer, primary_key=True, index=True)
    catname = Column(String)
    description = Column(String, nullable=True)
    datecreated = Column(DateTime, default=datetime.utcnow, nullable=False)
    