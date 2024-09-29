from fastapi import APIRouter,Depends, status, Response, HTTPException
from .. import schemas, database, models
from typing import List
from sqlalchemy.orm import Session
router = APIRouter(
    prefix="/blog",
    tags=["Blog"],
    responses={404: {"description": "Not found"}}
)

@router.post("/blog/",status_code=status.HTTP_201_CREATED, tags=["Blog"], response_model=schemas.Blog)
def create_blog(request: schemas.BlogCreate, db: Session = Depends(database.get_db)): 
    db_blog = models.Blog(title=request.title, description=request.description, is_published=request.is_published, user_id=1)
    db.add(db_blog)
    db.commit()
    db.refresh(db_blog)
    return db_blog

@router.get("/blog/", status_code=status.HTTP_200_OK, response_model=List[schemas.Blog] , tags=["Blog"])
def get_blogs(db: Session = Depends(database.get_db)):
    blogs = db.query(models.Blog).all()
    return blogs

@router.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Blog, tags=["Blog"])
def get_blog(id,response: Response ,db: Session = Depends(database.get_db)):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': 'Blog not found'}
    return blog

@router.delete("/blog/{id}", status_code=status.HTTP_200_OK, tags=["Blog"])
def delete_blog(id, db: Session = Depends(database.get_db)):
    db_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not db_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog id {id} not found")
    db_blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

@router.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Blog, tags=["Blog"])
def update_blog(id, request: schemas.BlogCreate, db: Session = Depends(database.get_db)):
    db_blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not db_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog id {id} not found")
    # db_blog.update(request.dict())
    db_blog.update({"title": request.title, "description": request.description, "is_published": request.is_published})
    db.commit()
    return db_blog.first()