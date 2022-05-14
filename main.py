from xmlrpc.client import DateTime
from fastapi import FastAPI
from datetime import datetime



app = FastAPI()


# ! BLOG ENDPOINT DEFINITION

@app.get('/blog/list')
def bloglist():
    return {'blogs-list': {
        'blog-1': 'this is the first blog',
        'blog-2': 'this is the second blog'
    }}
    
    
@app.get('/blog/view/{id}')
def get_blog(id: int):
    return {'blog': f'blog-{id} contents is listed here'}


@app.delete('blog/remove/{id}')
def del_blog(id: int):
    return {'blog': f'blog with {id} has been deleted'}


@app.post('/blog/create')
def create_blog(title: str, content: str, user: int):
    return {"message": f"blog with {title}, {content} created for user {user}"}

@app.put('/blog/update/{id}')
def udpate_blog(id: int):
    return {'blog': f'blog with id: {id},  has been updated'}


# ! CATEGORY ENDPOINT DEFINITION

@app.post('/category/create')
def create_category(catname: str):
    datecreated = datetime.utcnow  # type: ignore
    return {"message": f"category with {catname} created "}

@app.get('/category/list')
def get_categories():
    return {'cagegory-list':['food', 'economy', 'tech', 'news', 'crypto']}


@app.get('/category/view/{id}')
def get_category(id: int):
    return {'category': f'showing category with id {id}'}

@app.delete('category/remove/{id}')
def del_category(id: int):
    return {'category': f'category with {id} has been deleted'}


@app.put('/category/update/{id}')
def udpate_category(id: int):
    return {'category': f'category with id: {id},  has been updated'}


# ! USERS ENDPOINT DEFINITION
    
@app.get('/user/view/{id}')
def get_user(id: int):
    return {'user': f'viewing user with id: {id}'}


@app.delete('user/remove/{id}')
def del_user(id: int):
    return {'user': f'user with {id} has been deleted'}


@app.post('/user/create')
def create_user(fullname: str, email: str, mobile: str, password: str):
    return {"user": 
        f"user with fullname: {fullname}, email: {email}, mobile: {mobile}, created successfully."}

@app.put('/user/update/{id}')
def udpate_user(id: int):
    return {'user': f'user with id: {id},  has been updated'}


# ! AUTHENTICATION ENDPOINT DEFINITION

@app.post('/authentication/login')
def auth_login(email: str, password: str):
    return {'message': f'user with email: {email}, password: {password} authenticated successfully.'}

@app.post('/authentication/logout')
def auth_logout(id: int):
    return {'message': f'user with email: {id} logged out successfully.'}





