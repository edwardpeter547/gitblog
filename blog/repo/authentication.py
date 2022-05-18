from fastapi import HTTPException, status
from .. import models, schemas, jwtoken
from sqlalchemy.orm import Session
from .. hashing import Hash
from fastapi.security import OAuth2PasswordRequestForm


class AuthRepo():
    
    
    @classmethod
    def login(cls, request: OAuth2PasswordRequestForm, db: Session):
        user = db.query(models.User).filter(models.User.email == request.username).first()
        if not user:
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = f"invalid login credentials for user with email: {request.email}")
        if not Hash.verify(plain_password=request.password, hashed_password= user.password):
            raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = f"invalid login credentials for user with email: {request.email}")
        
        credentials = {"sub": user.email}
        access_token = jwtoken.create_access_token(user_data=credentials, expire_minutes=None)
        return {"access_token": access_token, "token_type": "bearer"}