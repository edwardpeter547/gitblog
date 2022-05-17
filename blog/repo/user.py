from sqlalchemy.orm import Session

from blog import schemas
from .. import models
from fastapi import HTTPException, status
from .. hashing import Hash

class UserRepo():
    
    
    @classmethod
    def list(cls, db: Session):
        users = db.query(models.User).all()
        if not users:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"no user has been created!")
        return users
    
    @classmethod
    def get(cls, id: int, db: Session):
        user = db.query(models.User).filter(models.User.id == id).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"user with id {id} not found!")
        return user
    
    
    @classmethod
    def delete(cls, id: int, db: Session):
        user = db.query(models.User).filter(models.User.id == id)
        if not user.first():
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"user with id {id} not found!")
        user.delete(synchronize_session=False) # type: ignore
        db.commit()
        return {"message": f'user with id: {id},  has been deleted'}
    
    
    @classmethod
    def create(cls, request: schemas.User, db: Session):
        hashed_password = Hash.encrypt(request.password)
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
    
    
    
    @classmethod
    def update(cls, id: int, request: schemas.User, db: Session):
        user = db.query(models.User).filter(models.User.id == id)
        if not user.first():
            raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"user with id {id} not found!")
        user.update(request.__dict__, synchronize_session=False) # type: ignore
        db.commit()
        return {"message": f"user with id: {id},  has been updated"}