from fastapi import APIRouter, status, Depends
from sqlalchemy.orm import Session
from .. import database, schemas, oauth
from .. repo.user import UserRepo


router = APIRouter(tags=["Users"], prefix="/user")

get_db = database.get_db


# Todo: list all users from db:
@router.get('/list', status_code = status.HTTP_200_OK)
def list_users(db: Session = Depends(get_db)):
    return UserRepo.list(db=db)


# Todo: show user with user id {id} from db:
@router.get('/view/{id}', status_code = status.HTTP_200_OK)
def get_user(id: int, db: Session = Depends(get_db)):
    return UserRepo.get(id=id, db=db)


# Todo: remove user with user id {id} from db:
@router.delete('/remove/{id}', status_code = status.HTTP_200_OK)
def del_user(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return UserRepo.delete(id=id, db=db)


# Todo: create user from User (schemas)
@router.post('/create')
def create_user(request: schemas.User, db: Session = Depends(get_db)):
    return UserRepo.create(request=request, db=db)


# Todo: update user with user id {id} from db
@router.put('/update/{id}', status_code = status.HTTP_200_OK)
def udpate_user(id: int, request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth.get_current_user)):
    return UserRepo.update(id=id, request=request, db=db)