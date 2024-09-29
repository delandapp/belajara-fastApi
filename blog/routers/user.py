from fastapi import APIRouter,Depends, status, Response, HTTPException
from .. import schemas, database, models
from ..hashing import Hash
from typing import List
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/user",
    tags=["User"],
    responses={404: {"description": "Not found"}}
)
@router.post('/user', response_model=schemas.User, status_code=status.HTTP_201_CREATED, tags=["User"])
def create_user(request: schemas.UserCreate, db: Session = Depends(database.get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user', response_model=List[schemas.User], tags=["User"])
def get_users(db: Session = Depends(database.get_db)):
    users = db.query(models.User).all()
    return users

@router.get('/user/{id}', response_model=schemas.User, tags=["User"])
def get_user(id, db: Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.id == id).first()
    return user