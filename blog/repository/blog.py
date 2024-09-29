from fastapi import status, HTTPException
from sqlalchemy import Integer
from sqlalchemy.orm import Session
from ..models import Blog

def get_all(db: Session):
    blogs = db.query(Blog).all()
    return blogs

def create_new(db: Session, request):
    blogs_new = Blog(title=request.title, description=request.description, is_published=request.is_published, user_id=1)
    db.add(blogs_new)
    db.commit()
    db.refresh(blogs_new)
    return blogs_new

def show_blog(db: Session, id: Integer):
    blog = db.query(Blog).filter(Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': 'Blog not found'}
    return blog

def delete_blog(db: Session, id: Integer):
    db_blog = db.query(Blog).filter(Blog.id == id)
    if not db_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog id {id} not found")
    db_blog.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_blog(db: Session, id, request):
    db_blog = db.query(Blog).filter(Blog.id == id)
    if not db_blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Blog id {id} not found")
    # db_blog.update(request.dict())
    db_blog.update({"title": request.title, "description": request.description, "is_published": request.is_published})
    db.commit()
    return db_blog.first()