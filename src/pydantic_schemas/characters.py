from pydantic import BaseModel, Field
from enum import Enum


class Status(str, Enum):
    alive = "Alive"
    dead = "Dead"
    unknown = "unknown"


class Gender(str, Enum):
    male = "Male"
    female = "Female"
    genderless = "Genderless"
    unknown = "unknown"


class Origin(BaseModel):
    name: str
    url: str


class Location(BaseModel):
    name: str
    url: str


class Character(BaseModel):
    id: int = Field(gt=0)
    name: str
    status: Status
    species: str
    type: str
    gender: Gender
    origin: Origin
    location: Location
    image: str
    episode: list
    url: str
    created: str


class Info(BaseModel):
    count: int = Field(gt=0, le=826)
    pages: int
    next: str = None
    prev: str = None


class Characters(BaseModel):
    info: Info
    results: list[Character]
