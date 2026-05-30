from pydantic import BaseModel
from typing import Union,Optional,List

class Developer(BaseModel):
    name: str
    experience: Optional[int] = None


class Projects(BaseModel):
    title: str
    description: Optional[str] = None
    language: Optional[List[str]] = None
    lead_developer: Developer



