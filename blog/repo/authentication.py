from fastapi import HTTPException, status
from .. import models, schemas
from sqlalchemy.orm import Session
from .. hashing import Hash


class AuthRepo():
    
    
    @classmethod
    def login(cls, request: schemas.Auth, db: Session):
        user = db.query(models.User).filter(models.User.email == request.email).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = f"email {request.email} is incorrect!")
        if not Hash.verify(plain_password=request.password, hashed_password= user.password):
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = f"email {request.email} is incorrect!")
        return {"message": f"user with email {request.email} has been logged in successfully."}