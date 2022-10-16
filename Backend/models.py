from sqlalchemy import DateTime, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base
from sqlalchemy.sql import func

#Create SQLALchemy models from the Base class
class Task(Base):       # module
    __tablename__ = "task"      # table name

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    create_time = Column(DateTime(timezone=True), nullable = False)
    ddl_time = Column(DateTime(timezone=True), nullable = False)
    user_id = Column(Integer, ForeignKey("myuser.id", ondelete="CASCADE", onupdate="CASCADE"))

    belong_user = relationship("User", backref="has_tasks")     #M-O

class User(Base):
    __tablename__ = "myuser"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String, nullable = False)
    email = Column(String, nullable = False, unique = True)
    password = Column(String, nullable = False)