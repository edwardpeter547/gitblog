from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(DATABASE_URL, echo=True)

session_local = sessionmaker(engine, autocommit=False, autoflush=False)

Base = declarative_base()