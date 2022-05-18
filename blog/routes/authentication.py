from fastapi import APIRouter, HTTPException, status, Depends
from .. import schemas, database, models
from sqlalchemy.orm import Session
from .. hashing import Hash
from .. repo.authentication import AuthRepo
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(tags=["Authentication"], prefix="/auth")

get_db = database.get_db


@router.post('/login')
def auth_login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    return AuthRepo.login(request=request, db=db) 