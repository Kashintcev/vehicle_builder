from typing import List, Optional
from pydantic import BaseModel


class Function(BaseModel):
    id: int
    name: str


class Feature(BaseModel):
    id: int
    name: str
    functions: Optional[List[Function]]


class Group(BaseModel):
    id: int
    name: str
    features: Optional[List[Feature]]
