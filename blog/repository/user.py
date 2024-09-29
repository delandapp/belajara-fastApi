from fastapi import status, HTTPException
from sqlalchemy import Integer
from sqlalchemy.orm import Session
from ..models import User
from ..hashing import Hash

def get_all(db: Session):
    users = db.query(User).all()
    return users

def create_new(db: Session, request):
    users_new = User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(users_new)
    db.commit()
    db.refresh(users_new)
    return users_new

def show_user(db: Session, id: Integer):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User id {id} not found")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': 'User not found'}
    return user

def delete_user(db: Session, id: Integer):
    db_user = db.query(User).filter(User.id == id)
    if not db_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User id {id} not found")
    db_user.delete(synchronize_session=False)
    db.commit()
    return 'done'

def update_user(db: Session, id, request):
    db_user = db.query(User).filter(User.id == id)
    if not db_user.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User id {id} not found")
    # db_user.update(request.dict())
    db_user.update({"name":request.name, "email":request.email, "password":Hash.bcrypt(request.password)})
    db.commit()
    return db_user.first()