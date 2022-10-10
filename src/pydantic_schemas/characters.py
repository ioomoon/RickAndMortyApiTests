from typing import Union

from pydantic import BaseModel, Field, HttpUrl, validator
from datetime import datetime
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
    url: Union[HttpUrl, str]

    @validator('url')
    def check_url(cls, v):
        if isinstance(v, str) and not isinstance(v, HttpUrl):
            assert v == ''
        return v


class Location(BaseModel):
    name: str
    url: Union[HttpUrl, str]

    @validator('url')
    def check_url(cls, v):
        if isinstance(v, str) and not isinstance(v, HttpUrl):
            assert v == ''
        return v


class Character(BaseModel):
    id: int = Field(gt=0)
    name: str
    status: Status
    species: str
    type: str
    gender: Gender
    origin: Origin
    location: Location
    image: HttpUrl
    episode: list[HttpUrl]
    url: HttpUrl
    created: datetime


class Info(BaseModel):
    count: int = Field(gt=0, le=826)
    pages: int
    next: Union[HttpUrl, None]
    prev: Union[HttpUrl, None]


class Characters(BaseModel):
    info: Info
    results: list[Character]
