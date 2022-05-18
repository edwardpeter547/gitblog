from pydantic import BaseModel, typing
from typing import Optional


class User(BaseModel):
    fullname: str
    email: str
    mobile: str
    password: str
    
    
    
class Blog(BaseModel):
    title: str
    content: str

class Category(BaseModel):
    catname: str
    description: str
    

class Auth(BaseModel):
    email: str
    password: str
    
    
class TokenData(BaseModel):
    email: Optional[str] = None
    
    


    
    