from pydantic import BaseModel, typing


class User(BaseModel):
    fullname: str
    email: str
    mobile: str
    datecreated: str
    
    
class Blog(BaseModel):
    title: str
    content: str
    datecreated: str

class Category(BaseModel):
    catname: str
    datecreated: str


    
    