from typing import Union

from pydantic import BaseModel

#Create Pydantic models/schemas

class TaskBase(BaseModel):
    name: str