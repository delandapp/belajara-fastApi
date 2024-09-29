from fastapi import APIRouter,Depends, status, Response, HTTPException
from .. import schemas, database, models
from ..hashing import Hash
from typing import List
from sqlalchemy.orm import Session
from ..repository import user
router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}}
)
@router.post('/user', response_model=schemas.User, status_code=status.HTTP_201_CREATED, tags=["User"])
def create_user(request: schemas.UserCreate, db: Session = Depends(database.get_db)):
    return user.create_new(db, request)

@router.get('/user', response_model=List[schemas.User], tags=["User"])
def get_users(db: Session = Depends(database.get_db)):
    return user.get_all(db)

@router.get('/user/{id}', response_model=schemas.User, tags=["User"])
def get_user(id, db: Session = Depends(database.get_db)):
    return user.show_user(db, id)

@router.put('/user/{id}', response_model=schemas.User, tags=["User"])
def edit_user(id, db:Session=Depends(database.get_db)):
    return user.update_user(db, id)

@router.delete('/user/{id}', response_model=schemas.User, tags=["User"])
def delete_user(id, db:Session=Depends(database.get_db)):
    return user.delete_user(db, id)