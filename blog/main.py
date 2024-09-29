from fastapi import FastAPI
from . import models
from .database import  engine
from .routers import blog, user

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

tags_metadata = [
    {
        "name": "Blog",
        "description": "Operations with blog",
    },
    {
        "name": "User",
        "description": "Operations with user",
    },
]

app.include_router(blog.router)
app.include_router(user.router)


# Dependency
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()


# @app.post("/blog/",status_code=status.HTTP_201_CREATED, tags=["Blog"], response_model=schemas.Blog)
# def create_blog(request: schemas.BlogCreate, db: Session = Depends(get_db)): 
#     db_blog = models.Blog(title=request.title, description=request.description, is_published=request.is_published, user_id=1)
#     db.add(db_blog)
#     db.commit()
#     db.refresh(db_blog)
#     return db_blog

# @app.get("/blog/", status_code=status.HTTP_200_OK, response_model=List[schemas.Blog] , tags=["Blog"])
# def get_blogs(db: Session = Depends(get_db)):
#     blogs = db.query(models.Blog).all()
#     return blogs

# @app.get("/blog/{id}", status_code=status.HTTP_200_OK, response_model=schemas.Blog, tags=["Blog"])
# def get_blog(id,response: Response ,db: Session = Depends(get_db)):
#     blog = db.query(models.Blog).filter(models.Blog.id == id).first()
#     if not blog:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog id {id} not found")
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'detail': 'Blog not found'}
#     return blog

# @app.delete("/blog/{id}", status_code=status.HTTP_200_OK, tags=["Blog"])
# def delete_blog(id, db: Session = Depends(get_db)):
#     db_blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not db_blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog id {id} not found")
#     db_blog.delete(synchronize_session=False)
#     db.commit()
#     return 'done'

# @app.put("/blog/{id}", status_code=status.HTTP_202_ACCEPTED, response_model=schemas.Blog, tags=["Blog"])
# def update_blog(id, request: schemas.BlogCreate, db: Session = Depends(get_db)):
#     db_blog = db.query(models.Blog).filter(models.Blog.id == id)
#     if not db_blog.first():
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"Blog id {id} not found")
#     # db_blog.update(request.dict())
#     db_blog.update({"title": request.title, "description": request.description, "is_published": request.is_published})
#     db.commit()
#     return db_blog.first()

# @app.post('/user', response_model=schemas.User, status_code=status.HTTP_201_CREATED, tags=["User"])
# def create_user(request: schemas.UserCreate, db: Session = Depends(get_db)):
#     new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
#     db.add(new_user)
#     db.commit()
#     db.refresh(new_user)
#     return new_user

# @app.get('/user', response_model=List[schemas.User], tags=["User"])
# def get_users(db: Session = Depends(get_db)):
#     users = db.query(models.User).all()
#     return users

# @app.get('/user/{id}', response_model=schemas.User, tags=["User"])
# def get_user(id, db: Session = Depends(get_db)):
#     user = db.query(models.User).filter(models.User.id == id).first()
#     return user