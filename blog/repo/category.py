from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status

class CategoryRepo():
    
    
    @classmethod
    def create(cls, request: schemas.Category, db: Session):
        new_cat = models.Category(catname = request.catname, description = request.description)
        db.add(new_cat)
        db.commit()
        db.refresh(new_cat)
        return new_cat
    
    
    @classmethod
    def list(cls, db: Session):
        categories = db.query(models.Category).all()
        if not categories:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"No category list found!")
        return categories
    
    
    @classmethod
    def get(cls, id: int, db: Session):
        category = db.query(models.Category).filter(models.Category.id == id).first()
        if not category:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"category with id {id} not found!")
        
        return category
    
    
    @classmethod
    def delete(cls, id: int, db: Session):
        category = db.query(models.Category).filter(models.Category.id == id)
        if not category.first():
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"category with id {id} not found!")
        category.delete(synchronize_session=False)   # type: ignore
        db.commit()
        return {"message": f"category with id {id} has been deleted!"}
    
    
    @classmethod
    def update(cls, id: int, db: Session):
        category = db.query(models.Category).filter(models.Category.id == id)
        if not category.first():
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"category with id {id} not found!")
        category.update(request.__dict__, synchronize_session=False) # type: ignore
        db.commit()
        return {"message": f'category with id: {id},  has been updated'}