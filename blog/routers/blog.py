from fastapi import APIRouter,Depends, status
from .. import schemas, database
from ..repository import blog
from typing import List
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
    responses={404: {"description": "Not found"}}
)

@router.post("/blog/",status_code=status.HTTP_201_CREATED, tags=["Blog"], response_model=schemas.Blog)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(database.get_db)): 
    return blog.create_new(db, request)

@router.get("/blog/", status_code=status.HTTP_200_OK, response_model=List[schemas.Blog] , tags=["Blog"])
def get_blogs(db: Session = Depends(database.get_db)):
    return blog.get_all(db)

@router.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Blog, tags=["Blog"])
def get_blog(id,db: Session = Depends(database.get_db)):
    return blog.show_blog(db, id)

@router.delete("/blog/{id}", status_code=status.HTTP_200_OK, tags=["Blog"])
def delete_blog(id, db: Session = Depends(database.get_db)):
    return blog.delete_blog(db,id)

@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Blog, tags=["Blog"])
def update_blog(id, request: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    return blog.update_blog(db, id, request)