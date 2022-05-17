from fastapi import APIRouter, Depends, status
from .. import schemas, database
from sqlalchemy.orm import Session
from .. repo.category import CategoryRepo



router = APIRouter(tags=["Post Category"], prefix="/category")

get_db = database.get_db


# Todo: create new category from Category (schema)
@router.post('/create', status_code = status.HTTP_201_CREATED)
def create_category(request: schemas.Category, db: Session = Depends(get_db)):
    return CategoryRepo.create(request=request, db=db)


# Todo: list all category from db:
@router.get('/list', status_code = status.HTTP_200_OK)
def get_categories(db: Session = Depends(get_db)):
    return CategoryRepo.list(db=db)



# Todo: view category with category id {id} from db:
@router.get('/view/{id}', status_code = status.HTTP_200_OK)
def get_category(id: int, db: Session = Depends(get_db)):
    return CategoryRepo.get(id=id, db=db)


# Todo: remove category with category id {id} from db:
@router.delete('/remove/{id}', status_code = status.HTTP_200_OK)
def del_category(id: int, db: Session = Depends(get_db)):
    return CategoryRepo.delete(id=id, db=db)


# Todo: update category with category id {id} from db:
@router.put('/update/{id}', status_code = status.HTTP_200_OK)
def udpate_category(id: int, request: schemas.Category, db: Session = Depends(get_db)):
    return CategoryRepo.update(id=id, db=db)
    