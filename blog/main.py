from fastapi import Depends, FastAPI, status, HTTPException
from datetime import datetime
from sqlalchemy.orm import Session
from . import models, schemas, hashing


app = FastAPI()

models.Base.metadata.create_all(models.engine)

def get_db():
    db = models.session_local()
    try:
        yield db
        
    finally:
        db.close()
        

# ! BLOG ENDPOINT DEFINITION

@app.get('/blog/list', status_code = status.HTTP_200_OK)
def bloglist(db: Session = Depends(get_db)):
    bloglist = db.query(models.Blog).all()
    if not bloglist:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"no post content found!")
    return bloglist
    
    
@app.get('/blog/view/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id {id} not found!")
    
    return blog


@app.delete('blog/remove/{id}', status_code = status.HTTP_200_OK)
def del_blog(id: int, db: Session = Depends(get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
    
    blog.delete(synchronize_session=False)   # type: ignore
    db.commit()
    return {"message:" f"post with id {id} has been deleted successfully."}


@app.post('/blog/create', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    
    blog = models.Blog(title=request.title, content = request.content)
    db.add(blog)
    db.commit()
    db.refresh(blog)
    return blog



@app.put('/blog/update/{id}', status_code = status.HTTP_200_OK)
def udpate_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    # query database for blog with selected post {id}
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    # check if post with id {id} exist
    if not blog.first():
        # raise HTTPException if post with {id} does not exist in the db
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"blog with id {id} not found!")
    
    new_post = models.Blog(title=request.title, content=request.content)
    blog.update(request.__dict__, synchronize_session=False)   # type: ignore
    db.commit()
    
    return {'message': f"post with id {id} updated successfully."}
    

# ! CATEGORY ENDPOINT DEFINITION

@app.post('/category/create', status_code = status.HTTP_201_CREATED)
def create_category(request: schemas.Category, db: Session = Depends(get_db)):
    new_cat = models.Category(catname = request.catname, description = request.description)
    db.add(new_cat)
    db.commit()
    db.refresh(new_cat)
    return new_cat
   

@app.get('/category/list', status_code = status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).all()
    if not categories:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"No category list found!")
    return categories
    


@app.get('/category/view/{id}', status_code = status.HTTP_200_OK)
def get_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id).first()
    if not category:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"category with id {id} not found!")
    
    return category

@app.delete('category/remove/{id}', status_code = status.HTTP_200_OK)
def del_category(id: int, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id)
    if not category.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"category with id {id} not found!")
    category.delete(synchronize_session=False)   # type: ignore
    db.commit()
    return {"message": f"category with id {id} has been deleted!"}
    


@app.put('/category/update/{id}', status_code = status.HTTP_200_OK)
def udpate_category(id: int, request: schemas.Category, db: Session = Depends(get_db)):
    category = db.query(models.Category).filter(models.Category.id == id)
    if not category.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"category with id {id} not found!")
    category.update(request.__dict__, synchronize_session=False) # type: ignore
    db.commit()
    return {"message": f'category with id: {id},  has been updated'}


# ! USERS ENDPOINT DEFINITION
    
@app.get('/user/list', status_code = status.HTTP_200_OK)
def list_users(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    if not users:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"no user has been created!")
    return users
    

@app.get('/user/view/{id}', status_code = status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"user with id {id} not found!")
    return user
    


@app.delete('/user/remove/{id}', status_code = status.HTTP_200_OK)
def del_user(id: int, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"user with id {id} not found!")
    user.delete(synchronize_session=False) # type: ignore
    db.commit()
    return {"message": f'user with id: {id},  has been deleted'}
    


@app.post('/user/create')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    hashed_password = hashing.Hash.encrypt(request.password)
    new_user = models.User(
        fullname = request.fullname, 
        email = request.email, 
        mobile = request.mobile, 
        password = hashed_password
        )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user
    
        

@app.put('/user/update/{id}', status_code = status.HTTP_200_OK)
def udpate_user(id: int, request: schemas.User, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.id == id)
    if not user.first():
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"user with id {id} not found!")
    user.update(request.__dict__, synchronize_session=False) # type: ignore
    db.commit()
    return {"message": f"user with id: {id},  has been updated"}


# ! AUTHENTICATION ENDPOINT DEFINITION

@app.post('/authentication/login')
def auth_login(request: schemas.Auth, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.email == request.email).first()
    if not user:
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = f"email {request.email} is incorrect!")
    if not hashing.Hash.verify(plain_password=request.password, hashed_password= user.password):
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = f"email {request.email} is incorrect!")
    return {"message": f"user with email {request.email} has been logged in successfully."}
    
    # return {'message': f'user with email: {email}, password: {password} authenticated successfully.'}

@app.post('/authentication/logout')
def auth_logout(id: int):
    return {'message': f'user with email: {id} logged out successfully.'}





