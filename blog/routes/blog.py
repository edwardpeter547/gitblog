from fastapi import APIRouter, status, Depends, HTTPException
from sqlalchemy.orm import Session
from .. import models, database, schemas, oauth
from .. repo.blog import Blogrepo


router = APIRouter(tags=["Post"], prefix="/post", dependencies=[Depends(oauth.get_current_user)])

get_db = database.get_db

# Todo: list all post from db:
@router.get('/list', status_code = status.HTTP_200_OK)
def bloglist(db: Session = Depends(get_db)):  # type: ignore
    return Blogrepo.list(db=db)


# Todo: get post with post id {id} from db:
@router.get('/view/{id}', status_code=status.HTTP_200_OK)
def get_blog(id: int, db: Session = Depends(get_db)):
    return Blogrepo.get(id=id, db=db)


# Todo: remove post with post id {id} from db:
@router.delete('/remove/{id}', status_code = status.HTTP_200_OK)
def del_blog(id: int, db: Session = Depends(get_db)):
    return Blogrepo.delete(id=id, db=db)


# Todo: create post using Blog from (schemas)
@router.post('/create', status_code=status.HTTP_201_CREATED)
def create_blog(request: schemas.Blog, db: Session = Depends(get_db)):
    return Blogrepo.create(request=request, db=db)


# Todo: update post with post id {id} from db:
@router.put('/update/{id}', status_code = status.HTTP_200_OK)
def udpate_blog(id: int, request: schemas.Blog, db: Session = Depends(get_db)):
    return Blogrepo.udpate(id=id, request=request, db=db)
