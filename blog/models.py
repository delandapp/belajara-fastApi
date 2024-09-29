from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from .database import Base
from sqlalchemy.orm import relationship

class Blog(Base):
    __tablename__ = "blogs"

    id = Column(Integer, primary_key=True,index=True)
    title = Column(String(100))
    description = Column(String(255)) 
    is_published = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    # Relasi User to colums blogs di table users
    creator = relationship("User", back_populates="blogs")
    
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True,index=True)
    name = Column(String(100))
    email = Column(String(255)) 
    password = Column(String(255))
    # Relasi Blog to colums creator di table blogs
    blogs = relationship("Blog", back_populates="creator")
    