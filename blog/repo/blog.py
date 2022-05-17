from sqlalchemy.orm import Session

from .. import models, schemas
from fastapi import HTTPException, status


class Blogrepo():
    
    @classmethod
    def list(cls, db: Session):
        bloglist = db.query(models.Blog).all()
        if not bloglist:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail = f"no post content found!")
        return bloglist
    
    @classmethod
    def get(cls, id: int, db: Session):
        blog = db.query(models.Blog).filter(models.Blog.id == id).first()
        if not blog:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post with id {id} not found!")
        
        return blog
    
    
    @classmethod
    def delete(cls, id: int, db: Session):
        blog = db.query(models.Blog).filter(models.Blog.id == id)
        if not blog.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post with id {id} not found")
        
        blog.delete(synchronize_session=False)   # type: ignore
        db.commit()
        return {"message:" f"post with id {id} has been deleted successfully."}
    
    
    @classmethod
    def create(cls, request: schemas.Blog, db: Session):
        blog = models.Blog(title=request.title, content = request.content)
        db.add(blog)
        db.commit()
        db.refresh(blog)
        return blog
    
    
    @classmethod
    def udpate(cls, id: int, request: schemas.Blog, db: Session):
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