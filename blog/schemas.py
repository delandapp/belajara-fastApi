from pydantic import BaseModel
from typing import List

class BlogBase(BaseModel):
    title: str
    description: str

class BlogCreate(BlogBase):
    title: str
    description: str
    is_published: bool
    
    class Config:
        orm_mode = True
        
class UserBase(BaseModel):
    name: str
    email: str
        
class User(UserBase):
    name: str
    email: str
    blogs: List[BlogBase] = []
    
    class Config:
        orm_mode = True
        
class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    
    class Config:
        orm_mode = True
        
class Blog(BlogBase):
    id: int
    title: str
    description: str
    is_published: bool
    creator: UserBase
    
    class Config:
        orm_mode = True