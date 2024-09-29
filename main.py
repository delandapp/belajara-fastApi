from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
app = FastAPI()

@app.get("/")
def index():
    return {'data':{'name': 'John', 'age': 30}, 'status' : 'success', 'code' : 200}

@app.get("/about")
def about():
    return {'data':{'name': 'John', 'age': 30, 'about': 'My name is John'}, 'status' : 'success', 'code' : 200}

# Query Parameter (blog?limit=10&published=true&sort=asc)
# Optional Parameters
@app.get("/blog")
def index(limit:int = 10, published:bool = True, sort: Optional[str] = None):
    if sort == 'desc':
        return {'data': f'Mengambil {limit} data,yang published {published}, sort {sort}', 'status' : 'success', 'code' : 200}
    else:
        return {'data': f'Mengambil {limit} data,yang published {published}, sort {sort}', 'status' : 'success', 'code' : 200}

# Path Parameter
@app.get("/blog/unpublished")
def unpublished():
    return {'data': 'All unpublished blog posts', 'status' : 'success', 'code' : 200}

@app.get("/blog/{id}")
def show(id:int):
    return {'data': id, 'status' : 'success', 'code' : 200}

@app.get("/blog/{id}/comments")
def show(id:int, limit:int = 10, published:bool = True, sort: Optional[str] = None):
    return {'data': {'id': id, 'comments': ['comment 1', 'comment 2'], 'limit': limit, 'published': published, 'sort': sort}, 'status' : 'success', 'code' : 200}

# Post Method
@app.post("/blog")
def create():
    return {'data': 'blog created', 'status' : 'success', 'code' : 200}


# Form Body Request

# Create class extends BaseModel from pydantic
class Blog (BaseModel):
    title: str
    body: str
    published: Optional[bool]

@app.post("/create/blog")
def create_blog(request: Blog):
    return {'data': request, 'status' : 'success', 'code' : 200}