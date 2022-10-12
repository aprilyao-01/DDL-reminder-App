from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base


#Create SQLALchemy models from the Base class
class Task(Base):
    __tablename__ = "Task"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    create_time = Column(String, nullable = False)
    ddl_time = Column(String, nullable = False)
    user_id = Column(Integer, ForeignKey("User.id", ondelete="CASCADE", onupdate="CASCADE"))

    belong_user = relationship("User", backref="has_tasks")     #M-O

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)